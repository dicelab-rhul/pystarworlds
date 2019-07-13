"""
@author: Nausheen Saba Shahid
"""

from .Identifiable import Identifiable
from .Perception import Perception
from .Factories import PerceptionFactory,RuleFactory,ActionFactory

class Environment(Identifiable):
    
    def __init__(self, physics, ambient,actions,sensors):  #,events): not used 
        self.__physics__= physics
        self.__ambient__ = ambient
        self.__actions__ = actions
        self.__sensors = sensors
        self.subscriptionSetup(sensors)
        self.time=1
        self.attempts=[]
        self.end=False
        self.perception_factories = []
        self.rule_factories = []
        self.executeaction_factories=[]
      
        
    def setupFactories(self):
        self.perception_factories = [PerceptionFactory()]
        self.rule_factories = [RuleFactory()]
        self.executeaction_factories = [RuleFactory()]
        
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
            
#########################################################################
        
    def simulate(self, cycles):
        self.setupFactories()
        i=0
        while(i<cycles):
           
          print("_______________________________________________________________________________")
          print("_______________________________________________________________________________")
          print("  Time stamp ")
          print(i)
        
          self.evolveEnvironment()   
          i=i+1
                  
    def evolveEnvironment(self):
        for perception_factory in self.perception_factories:
            self.getPhysics().notify_perceptions(self,perception_factory)
        
        agents=self.getAmbient().agents
        for a in agents:
            a.cycle()
            
        attempts=self.retrievingAttempts(agents) 
        self.getPhysics().execute(attempts,self,self.getActions(),self.rule_factories,self.executeaction_factories)
        
        print(agents)
        print(attempts)       
    
    def retrievingAttempts(self,agents):   
        attempts=[] 
        for a in agents:
           for ac in a.getActuators():
                tempact=ac.act()
                
                if(tempact!=0):
                 attempts.append(tempact) 
      
        return attempts   
        
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    
class Ambient(Identifiable):
    
    def __init__(self, agents, objects):
        self.agents = agents
        #what is this conceptually?
        self.objects = objects
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
  
    
    
    
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

   
   def execute(self,attempts,env,valid_actions,rule_factories,executeaction_factories):
      
       for act in attempts:
           if type(act) in valid_actions:
               for rule_factory in rule_factories:
                  if(type(act)==rule_factory._type) and rule_factory(env,act):
                   for executeaction_factory in executeaction_factories:
                      if (type(act)==executeaction_factory._type):     
                         executeaction_factory(env,act)
                   
                   
   #this is general ( a general notification mechanism for sensors)                  

   def notifySinglePerception(self,per):
         sensors = self.EventSensorsDirectory[type(per)] # get type of all sensors to be notified
         for s in sensors:
           if(s.getOwner()==(per.getOwner())):
             s.notifyEvent(per)
   def notify_perceptions(self,env, perception_factory):
       # Notify all agents who have sensor of that factory type  
    
        sensors = self.EventSensorsDirectory[perception_factory._type]
     

        for ag in env.getAmbient().agents:
            if len(sensors) > 0:
                for s in sensors:
                   if(s.getOwner()==(ag.getID())):
                     perception = perception_factory(env, ag, s)
                     s.notifyEvent(perception)      
   
  
   











