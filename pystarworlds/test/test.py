#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:42:37 2019

@author: ben
"""

from pystarworlds.Environment import Environment, Ambient, Physics
from pystarworlds.Action import Action
from pystarworlds.Agent import Body, Mind, Actuator, Sensor

class _Ambient(Ambient):
    
    def __init__(self, agents, objects):
        super(_Ambient, self).__init__(agents, objects)

class _Action(Action):
    precondition = lambda env, action: True
    executor = lambda env, action: None #do nothing
    pass

class Perception(Perception):
    pass

class _Mind(Mind):
    
    def cycle(self):
        pass
    
class _Actuator(Actuator):
    pass

class _Sensor(Sensor):
    subscribed = []
    pass
    

agents = [Body(_Mind(), [_Sensor()], [_Actuator()])]
actions = [_Action]
physics = Physics(actions)
ambient = Ambient(agents)

e = Environment(physics,ambient,None)