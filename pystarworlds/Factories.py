# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 13:38:02 2019

@author: Nausheen Saba
"""




class PerceptionFactory:
    
    def __init__(self, _type):
        self._type = _type
      
        print(self._type)
        
    def __call__(self, environment, agent,sensor):
        pass
    

class RuleFactory:
    
    def __init__(self, _type):
        self._type = _type
      
        
    def __call__(self, attempts, environment, actions):
        pass
    

class ActionFactory:
    
    def __init__(self, _type):
        self._type = _type
      
        print(self._type)
        
    def __call__(self, actorName,orient,currentcoordinate):
        pass
    


