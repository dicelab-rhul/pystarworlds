"""
@author: Nausheen Saba Shahid
@author: Benedict Wilkins
"""

from .Identifiable import Identifiable
from .Event import Transient

class Sensor(Identifiable,Transient):
    
    def __init__(self,compatibilitylist):
       super(Sensor, self).__init__()
       self.owner = None
       #self.__compatibility__=compatibilitylist
   
    def notifyEvent(self,event):
        super(Sensor, self).sink(event)
        
''' think about this
  def isCompatible(self, per):
       flag=False
       for com in self.__compatibility__:   
        if(type(per)==com):
         flag=True
       return flag   
'''
   
''' No. use -> for percept in sensor:
    def getPercepion(self):
        perceptionLis t =[] 
        while(super().isEmpty()==False):
          perceptionList.append(super().source())   
        return perceptionList
        
'''
  
    
