
from BasicBuildingBlock.Identificaiton import Identifiable
from BasicBuildingBlock.Event import Transient


class Actuator(Transient, Identifiable):
  
    def __init__(self,compatibilitylist):
        super().__init__()
        self.__isWorking__= True;
        self.__compatibility__=compatibilitylist
        
        
    def isCompatible(self, action):
       flag=False
       for com in self.__compatibility__:   
        if(type(action)==com):
         flag=True
       return flag    
   
    def attempt(self, action):
         super().sink(action)
  
     
    def act(self):
         if (super().isEmpty()):
             return 0
         else:
             return super().source()

    
    def isWorking(self):
        return self.__isWorking__        
    def setEnabled(self):
        self.__isWorking__=True
    def setDisabled(self):
        self.__isWorking__=False
            
        
    def noActionsPending(self):
        return super().isEmpty()  
    
    def getOwner(self):        # Retrieves the sensor's associated agent
        return self.__owner__ 
    
    def setOwner(self,ag1):        # Retrieves the sensor's associated agent
        self.__owner__=ag1


