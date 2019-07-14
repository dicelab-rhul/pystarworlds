"""
@author: Nausheen Saba Shahid
@author: Benedict Wilkins
"""

from .Identifiable import Identifiable
#from .Perception import Perception

class Environment(Identifiable):
    
    def __init__(self, physics, ambient, processes, actions, sensors):  #,events): not used 
        self.physics = physics
        self.ambient = ambient
        self.actions = actions
        self.sensors = sensors
        self.physics.makeSubscriptionDirectory(sensors)
        self.time=1
        self.attempts=[]
        self.end=False
        self.perception_factories = []
        self.rule_factories = []
        self.executeaction_factories=[]
        
        self.events = []
        self.processes = processes
      
   
        
            
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
        for process in self.processes:
            print("process:", process)
            process(self) #allow all processes to do their thing

        
        agents=self.ambient.agents.values()
        for a in agents:
            a.cycle()
            
        #attempts=self.retrievingAttempts(agents) 
        attempts = [action for agent in agents for actuator in agent.actuators() for action in actuator]
        self.physics.execute(self.ambient, attempts, self.rule_factories, self.executeaction_factories)
        
        print("AGENTS:", agents)
        print("ATTEMPTS:", attempts)       
        
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    
class Ambient(Identifiable):
    
    def __init__(self, agents, objects):
        self.agents = {ag.ID:ag for ag in agents}
        self.objects = {obj.ID:obj for obj in objects} #what is this conceptually?  
    
    
class Physics(Identifiable):
         
    def __init__(self, mapping):
        self.sensor_event_mapping = mapping #{VisionSensor:[VisionPerception,GridVisionPerception], CommunicationSensor:[CommunicationAction]}
        self.subscriptions = {}
      
    def subscribe_event(self, sensor,temp_list):
          s=type(sensor)
          self.sensor_event_mapping[s]=temp_list
        
    #names! subscription,
    def makeSubscriptionDirectory(self, sensors):
       sub_dict = {e:[] for k,v in self.sensor_event_mapping.items() for e in v}
       for s in sensors:   
           events = self.sensor_event_mapping[type(s)]
           for e in events:
               sub_dict[e].append(s) 
       self.subscriptions=sub_dict
       
    def notify_agent(self, agent, event):
        for sensor in agent.sensors():
            print(sensor)
            if self.sensor_event_mapping.get(type(sensor), None):
                print("notify", sensor)
                sensor.notify(event)

    def execute(self, ambient, attempts, rules, executors):
        for attempt in attempts:
            if rules[type(attempt)](ambient, attempt): #this is checking a pre-condition
                executors[type(attempt)](ambient, attempt) #make changes to the ambient
        
''' No.
   def execute(self,attempts,env,valid_actions,rule_factories,executeaction_factories):
       for act in attempts:
           if type(act) in valid_actions:
               for rule_factory in rule_factories:
                  if(type(act)==rule_factory._type) and rule_factory(env,act):
                   for executeaction_factory in executeaction_factories:
                      if (type(act)==executeaction_factory._type):     
                         executeaction_factory(env,act)
                        
'''          
            
                
   
  
   











