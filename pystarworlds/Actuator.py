"""
@author: Nausheen Saba Shahid
"""
from .Identifiable import Identifiable
from .Event import Transient

class Actuator(Transient, Identifiable):
  
    def __init__(self,compatibilitylist):
        super(Actuator, self).__init__()
        self.owner = None
        #self.__isWorking__= True;
        #self.__compatibility__=compatibilitylist
        
    def attempt(self, action):
        super(Actuator, self).sink(action)
'''
    def isCompatible(self, action):
       flag=False
       for com in self.__compatibility__:   
        if(type(action)==com):
         flag=True
       return flag    
'''
   


