"""
@author: Nausheen Saba Shahid
@author: Benedict Wilkins
"""

from .Identifiable import Identifiable
#from .Perception import Perception
from collections import defaultdict

class Environment(Identifiable):
    
    def __init__(self, physics, ambient, processes=[], *args):  
        self.physics = physics
        self.ambient = ambient
        #self.actions = actions
        #self.attempts = [] 
        self.processes = processes
        
        #move this to the physics ...?
        self.physics.makeSubscriptionDirectory(self.ambient.agents.values())        
            
#########################################################################
        
    def simulate(self, cycles):
        self.setupFactories()
        i=0
        while(i<cycles):
           
          #print("_______________________________________________________________________________")
          #print("_______________________________________________________________________________")
          #print("  Time stamp ")
          #print(i)
        
          self.evolveEnvironment()   
          i=i+1
                  
    def evolveEnvironment(self):
        for process in self.processes:
            process(self) #allow all processes to do their thing

        
        agents=self.ambient.agents.values()
        for a in agents:
            a.cycle()
            
        attempts = [action for agent in agents for actuator in agent.actuators() for action in actuator]
        self.physics.execute(self, attempts)
        
        #print("AGENTS:", agents)
        #print("ATTEMPTS:", attempts)       
        
    def __str__(self):
        return super().__str__() + "~"+  str(self.__ambient__)
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
    
class Ambient(Identifiable):
    
    def __init__(self, agents, objects=[]):
        self.agents = {ag.ID:ag for ag in agents}
        self.objects = {obj.ID:obj for obj in objects} #what is this conceptually?  
    
class Physics(Identifiable):
         
    def __init__(self, actions, default_precondition = lambda action, ambient: True): #mapping, preconditions, executors, ):
        self.sensor_event_mapping = mapping #{VisionSensor:[VisionPerception,GridVisionPerception], CommunicationSensor:[CommunicationAction]}
        self.subscriptions = {}
        self.actions = actions
        self.preconditions = defaultdict(lambda : default_precondition, {action:action.precondition for action in self.actions})
        self.executors = {action:action.executor for action in self.actions}
     
    def __post_init__(self, agents):
        sensors = [s for a in agents for s in a.sensors()]
        sensor_types = {s.type for s in sensors}
        
        self.subscription_dict
        
        for s in sensors:
            
        
        
        '''
        sub_dict = {e:[] for k,v in self.sensor_event_mapping.items() for e in v}
        for s in sensors:   
            events = self.sensor_event_mapping[type(s)]
            for e in events:
                sub_dict[e].append(s) 
        self.subscriptions=sub_dict
        '''
        
       
       
    def notify_agent(self, agent, event):
        for sensor in agent.sensors():
            if type(event) in sensor.
                #print("notify", sensor)
                sensor.notify(event)

    def execute(self, env, attempts):
        for attempt in attempts:
            #print(attempt)
            #print(self.preconditions[type(attempt)])
            if self.preconditions[type(attempt)](env, attempt): #this is checking a pre-condition
                self.executors[type(attempt)](env, attempt) #make changes to the ambient
        
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

class Process(Identifiable):
    
    def __init__(self):
        pass
    
    def __call__(self, ambient):
        pass #return a list of events
            
                
   
  
   











