"""
@author: Nausheen Saba Shahid
"""
from .Event import Event

class Action(Event):
    
    def __init__(self,actor):
        super().__init__()
        self.__actor__=actor 
    
    def execute(self, env):   # not using this code currently
      pass
    def is_possible(self,acts):
        
        for a in acts:
         if(a.isCompatible(self)):
             return True
         return False 
    
    def getActor(self):
       return self.__actor__
    def setActor(self, actor):
        self.__actor__=actor

    def isSame(self):
        pass