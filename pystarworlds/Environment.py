
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

    #then cheap and bad way.. research is needed.
    def execute(self,attempts,ambient, valid_actions):
       for act in attempts:
           if act in valid_actions:
             if self.is_possible[type(act)](act, ambient):
                 self.execute_action[type(act)](act, ambient)
   
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
            
    def notify_perceptions(self, perception_factory):
        for ag in self.getAmbient().getAgents():
            sensors = self.getPhysics().EventSensorsDirectory[perception_factory._type]
            if len(sensors) > 0:
                for s in sensors:
                    perception = perception_factory(self, ag, s)
                    s.notifyEvent(perception)
                 


#########################################################################
    
                  
    def evolveEnvironment(self, perception_factories):
        for perception_factory in perception_factories:
            self.notify_perceptions(perception_factory)
        
        agents=self.getAmbient().getAgents()
        for a in agents:
            a.cycle()
            
        attempts=self.retrievingAttempts(agents) 
        ###### one step 
        validityvalues=self.getPhysics().verifyAttempts(attempts,self.getAmbient(),self.getActions())
        self.executeActions(attempts,validityvalues)
        ######        
    
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
        
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
   

class PerceptionFactory:
    
    def __init__(self, _type):
        self._type = _type
        
    def __call__(self, env, agent, sensor):
        pass
    









