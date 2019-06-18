from BasicBuildingBlock.Identificaiton import Identifiable

class Mind(Identifiable):
       
    def __post_init__(self, agentbody):
        self.__agentbody__ = agentbody
        self.__perceptions__=[]
    #@abstractmethod
    def cycle(self):
        
      self.revise()
      self.perceive()
      self.decide()
   
    def getAgent(self):
        return self.__agentbody__
    def revise(self):
        pass
    def perceive(self):
        self.__perceptions__=[]
        sensors=self.getAgent().getSensors()
        for s in sensors:
          if(s.isEmpty()==False):  # add perception 
             self.__perceptions__.extend(s.getPercepion())
        
    def decide(self):  # deliberate
        pass
    
    def execute(self,ambient,action):  
        action.execute(ambient)
        self.__perceptions__=[]# empty for next cycle
         
    def getPerceptions(self):
       return self.__perceptions__ 
    def attempt(self, actions):
       pass

#######################################

class AgentBody(Identifiable):
    
    def __init__(self, mind, actuators, sensors):
        self.__mind__ = mind
        if isinstance(actuators, dict) or isinstance(actuators, list) or isinstance(actuators, tuple):
            self.__actuators__ = actuators
            for a in self.__actuators__:
                a.setOwner(self.getID())
        else:
            raise ValueError("actuators must be a dict, list or tuple")
        if isinstance(sensors, dict) or isinstance(sensors, list) or isinstance(sensors, tuple):
            self.__sensors__ = sensors
            for s in self.__sensors__:
                s.setOwner(self.getID())
        else:
            raise ValueError("sensors must be a dict, list or tuple")
        self.__mind__.__post_init__(self)
         
    def cycle(self):
        
        return self.__mind__.cycle()
    
    def actuators(self):
        return list(self.__actuators__.values())
    
    def sensors(self):
        return list(self.__sensors__.values())
    
    def getSensors(self):
        return self.__sensors__
    def getActuators(self):
        return self.__actuators__
    
    def __hash__(self):
        return self.ID.__hash__()
        
    def __eq__(self):
        return self.ID.__eq__()

    def getMind(self):
        return self.__mind__
   
    def getID(self):
        return self.ID# -*- coding: utf-8 -*-

