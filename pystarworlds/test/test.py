#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:42:37 2019

@author: ben
"""

from Environment import Environment, Ambient, Physics
from Action import Action
from Agent import Body, Mind

class _Ambient(Ambient):
    
    def __init__(self, agents, objects):
        super(_Ambient, self).__init__(agents, objects)

class _Action(Action):
    precondition = lambda env, action: True
    executor = lambda env, action: None #do nothing
    pass

class _Mind(Mind):
    
    def cycle(self):
        pass
    
class _Actuator()
    

agents = 
actions = [_Action]
physics = Physics(actions)
ambient = Ambient()

e = Environment(physics,ambient,processes)