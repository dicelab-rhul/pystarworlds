
from BasicBuildingBlock.Identificaiton import Identifiable
from BasicBuildingBlock.Perception import Perception

class Ambient(Identifiable):
    def __init__(self, agents,objects):
        self.__agents__ = agents
        self.__objects__ = objects
    def getAgents(self):
        return self.__agents__
    def getObjetcs(self):
        return self.__objects__
    def __unicode__(self):
        return self.__str__()
    def __repr__(self):
        return self.__str__()
   # def getActuators(self, agentId):
    #    for a in self.getAgents():
      #      a.getId(agentId)
    
    
    
class Physics(Identifiable):
         
   def __init__(self, mapping):
      self.__sensorEventMapping__=mapping #{VisionSensor:[VisionPerception,GridVisionPerception], CommunicationSensor:[CommunicationAction]}
      self.EventSensorsDirectory={}
      
      
   
   def subscribe_event(self, sensor,temp_list):
    s=type(sensor)
    self.__sensorEventMapping__[s]=temp_list
    
  
        
   def makeSubscribtionDirectory(self, sensors):
       sub_dict = {e:[] for k,v in self.__sensorEventMapping__.items() for e in v}
       for s in sensors:
        events = self.__sensorEventMapping__[type(s)]
        for e in events:
         sub_dict[e].append(s) 
       self.set_SubscribtionRegistry(sub_dict)  
       

   def get_SubscribtionSize(self):
    return self.EventSensorsDirectory__.items()

   def get_eventsOfSensor(self,s):     
    return self.EventSensorsDirectory[type(s)]

   def get_SubscribtionRegistry(self):     
    return self.EventSensorsDirectory

   def set_SubscribtionRegistry(self,sub_dict):     
    self.EventSensorsDirectory=sub_dict     
   
   def isPossible(self, act,ambient,actions):
    pass

   def verifyAttempts(self,attempts,ambient,valid_actions):
     pass

   
   
class Environment(Identifiable):
    
    def __init__(self, physics, ambient,actions,sensors):  #,events): not used 
        self.__physics__= physics
        self.__ambient__ = ambient
        self.__actions__=actions
        self.__sensors=sensors
        self.subscriptionSetup(sensors)
        self.time=1
        self.attempts=[]
        self.end=False
        
    def getAmbient(self):
        return self.__ambient__
    def getPhysics(self):
        return self.__physics__  
    def getActions(self):
        return self.__actions__
    def getSensors(self):
        return self.__sensors
    def subscriptionSetup(self, sensors):    
        self.__physics__.makeSubscribtionDirectory(sensors)
    
    def notifyPerception(self):   
        for ag in self.getAmbient().getAgents(): 
          per1=Perception(ag.getID())
          sensors = self.getPhysics().EventSensorsDirectory[type(per1)] # get type of all sensors to be notified
          for s in sensors:
           if(s.getOwner()==(per1.getOwner())):
            s.notifyEvent(per1)
            
          
#########################################################################
    
                  
    def evolveEnvironment(self):
        
        agents=self.getAmbient().getAgents()
       
        self.evolutionStep(agents)
        attempts=self.retrievingAttempts(agents) 
        validityvalues=self.getPhysics().verifyAttempts(attempts,self.getAmbient(),self.getActions())
        self.executeActions(attempts,validityvalues)
    
    def evolutionStep(self,agents):   
      
        for a in agents:
            a.cycle()
            
        
           
        
   
    
    def retrievingAttempts(self,agents):   
        attempts=[] 
        for a in agents:
           for ac in a.getActuators():
                tempact=ac.act()
                
                if(tempact==0):
                 print("zero")
                else:  
                 attempts.append(tempact) 
        print(len(attempts))
        return attempts   
         
              
    def executeActions(self,attempts,validityvalues):      
           pass
        
        
     
 
        
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
   











