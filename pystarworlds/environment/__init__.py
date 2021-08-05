#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 20-11-2020 15:22:19

    [Description]
"""
__author__ = "Benedict Wilkins, Nausheen Saba Shahid"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

from collections import defaultdict

from ..common import Identifiable
from ..event import Transient, Source

class Environment(Identifiable):
    
    def __init__(self, physics, ambient, *args, **kwargs):
        super(Environment, self).__init__(*args, **kwargs)

        self.physics = physics
        self.ambient = ambient
        for agent in ambient.agents.values():
            self.physics.subscribe(agent)

    
    def simulate(self, cycles=1):
        for i in range(cycles):
            self.evolve()   

    def evolve(self):
        # TODO process events in order  ? this is probably quite a complex issue, currently processes execute first, then agents

        for process in self.ambient.processes.values():
            self.physics.execute(self, [e for e in process])

        for obj in self.ambient.objects.values():
            self.physics.execute(self, [e for e in obj])

        agents = self.ambient.agents.values()
        for a in agents:
            a.cycle()
            
        attempts = [action for agent in agents for actuator in agent.actuators.values() for action in actuator]
        self.physics.execute(self, attempts)
    
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    
class Ambient(Identifiable):
    
    def __init__(self, agents, objects=[], processes=[]):
        self.agents = {ag.ID:ag for ag in agents}
        self.objects = {obj.ID:obj for obj in objects}
        self.processes = {proc.ID:proc for proc in processes} 
    
class Physics(Identifiable):
         
    def __init__(self, actions): 
        self.subscriptions = defaultdict(list)
        self.actions = actions
        self.executors = defaultdict(lambda: self.notify)
        self.executors.update({action:action.executor(action) for action in self.actions})
       
    def subscribe(self, agent):
        for sensor in  agent.sensors.values():
            for sub in sensor.subscribe:
                self.subscriptions[sub].append(sensor)
    
    def notify(self, _, event): #used as an executor TODO refactor?
        for sensor in self.subscriptions[type(event)]:
            sensor.notify(event)

    def notify_agent(self, agent, event):
        #TODO rethink this?
        for sensor in agent.sensors.values():
            if type(event) in sensor.subscribe:
                sensor.notify(event)

    def execute(self, env, events):
        result = []
        for event in events:
            new_events = self.executors[type(event)](env, event)
            if new_events is not None:
                result.extend(new_events)
                
        if len(result) > 0:
            self.execute(env, result)    

class Object(Identifiable, Transient):
    pass 

class Process(Identifiable, Source):
    pass 
            
   
   
  
   











