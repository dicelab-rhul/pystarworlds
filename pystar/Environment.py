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
        #self.physics.__post_init__(self.ambient.agents.values())        
            
#########################################################################
        
    def simulate(self, cycles=1):
        for i in range(cycles):
            self.evolveEnvironment()   

                  
    def evolveEnvironment(self):
        #allow all processes to do their thing
        for process in self.processes:
            process(self) #TODO fix this, processes should return events!

        agents = self.ambient.agents.values()
        for a in agents:
            a.cycle()
            
        attempts = [action for agent in agents for actuator in agent.actuators() for action in actuator]
        events = self.physics.execute(self, attempts)
        
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
        print([ag for ag in self.agents])
        print([ag.ID for ag in self.agents.values()])
        self.objects = {obj.ID:obj for obj in objects} #what is this conceptually?  
    
class Physics(Identifiable):
         
    def __init__(self, actions): 
        self.subscriptions = defaultdict(list)
        self.actions = actions
        self.executors = {action:action.executor(action) for action in self.actions}
     
    def __post_init__(self, agents):
        sensors = [s for a in agents for s in a.sensors()]
        for sensor in sensors:
            for sub in sensor.subscribe:
                self.subscriptions[sub].append(sensor)

    def notify_agent(self, agent, event):
        #rethink this
        for sensor in agent.sensors():
            if type(event) in sensor.subscribe:
                sensor.notify(event)

    def execute(self, env, attempts):
        events = []
        for attempt in attempts:
            #print(attempt)
            #print(self.preconditions[type(attempt)])
           # if self.preconditions[type(attempt)](ambient, attempt): #this is checking a pre-condition
           new_events = self.executors[type(attempt)](env, attempt) #make changes to the ambient
           if new_events:
               events.extend(new_events)
        return events #events were generated by executing the actions
        
        
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
            
                
   
  
   










