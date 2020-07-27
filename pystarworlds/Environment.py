"""
@author: Nausheen Saba Shahid
@author: Benedict Wilkins
"""

from .Identifiable import Identifiable
#from .Perception import Perception
from collections import defaultdict

class Environment(Identifiable):
    
    def __init__(self, physics, ambient, processes=[], *args):  
        self.physics = physics
        self.ambient = ambient
        for agent in ambient.agents.values():
            self.physics.subscribe(agent)

        self.processes = processes
    
    def simulate(self, cycles=1):
        for i in range(cycles):
            self.evolveEnvironment()   

    def evolve(self):
        self.evolveEnvironment()
                  
    def evolveEnvironment(self): #TODO remove in favour of evolve
        #allow all processes to do thier thing
        for process in self.processes:
            events = process(self)
            self.physics.execute(self, events)

        agents = self.ambient.agents.values()
        for a in agents:
            a.cycle()
            
        attempts = [action for agent in agents for actuator in agent.actuators.values() for action in actuator]
        events = self.physics.execute(self, attempts)
    
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    
class Ambient(Identifiable):
    
    def __init__(self, agents, objects=[]):
        self.agents = {ag.ID:ag for ag in agents}
        self.objects = {obj.ID:obj for obj in objects} #what is this conceptually?  
    
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
           new_events = self.executors[type(event)](env, event) #make changes to the ambient
           if new_events is not None:
               result.extend(new_events)
        return result
        
        
''' No.
   def execute(self,attempts,env,valid_actions,rule_factories,executeaction_factories):
       for act in attempts:
           if type(act) in valid_actions:
               for rule_factory in rule_factories:
                  if(type(act)==rule_factory._type) and rule_factory(env,act):
                   for executeaction_factory in executeaction_factories:
                      if (type(act)==executeaction_factory._type):     
                         executeaction_factory(env,act)
                        
'''          

class Process(Identifiable):
    
    def __init__(self):
        pass
    
    def __call__(self, env):
        pass #return a list of events
            
                
   
  
   











