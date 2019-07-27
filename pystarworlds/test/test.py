#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:42:37 2019

@author: ben
"""

from pystarworlds.Environment import Environment, Ambient, Physics
from pystarworlds.Event import Action, Perception
from pystarworlds.Agent import Body, Mind, Actuator, Sensor

class _Physics(Physics):
    pass

class _Ambient(Ambient):
    
    def __init__(self, agents):
        super(_Ambient, self).__init__(agents)
        self.ACTION_TEST = False
        
    def action_test(self):
        self.ACTION_TEST = True

class _Action(Action):
    executor = lambda ambient, action: ambient.action_test()

class _Perception(Perception):
    pass

class _Mind(Mind):
    
    def cycle(self):
        action = _Action()
        self.body.find_actuators(action)[0].attempt(action)
    
class _Actuator(Actuator):
    subscribe = [_Action]
    
    def __init__(self):
        super(_Actuator, self).__init__()
        self.ACTUATOR_TEST = False
    
    def attempt(self, action):
        self.ACTUATOR_TEST = True
        super(_Actuator, self).attempt(action)
        
class _Sensor(Sensor):
    subscribe = [_Perception]
    
    def __init__(self):
        super(_Sensor, self).__init__()
        self.SENSOR_TEST = False
        
    def notify(self, perception):
        self.SENSOR_TEST = True

actuator = _Actuator()
sensor = _Sensor()
agents = [Body(_Mind(), [actuator], [sensor])]
actions = [_Action]
physics = _Physics(actions)
ambient = _Ambient(agents)

e = Environment(physics,ambient)

e.simulate()


assert ambient.ACTION_TEST 
assert actuator.ACTUATOR_TEST
assert sensor.SENSOR_TEST