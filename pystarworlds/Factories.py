# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:38:02 2019

@author: Nausheen Saba
@author: Benedict Wilkins
"""

class PerceptionFactory:
    
    def __init__(self, _type):
        self._type = _type
        
    def __call__(self, ambient, sensor):
        pass
    

class Rule:
    
    def __init__(self, _type):
        self._type = _type
      
    def __call__(self, ambient, events):
        pass
    

class Executor:
    
    def __init__(self, _type):
        self._type = _type
        
    def __call__(self, ambient, events):
        pass
    


