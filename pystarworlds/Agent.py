"""
@author: Nausheen Saba Shahid
@author: Benedict Wilkins
"""

#from ABC import abstractmethod

from .Identifiable import Identifiable
from .Event import Transient


class Mind:
       
    def __post_init__(self, body):
        self.body = body
        
    #@abstractmethod
    #def cycle(self):
    #    pass

#######################################

class Body(Identifiable):
    
    def __init__(self, mind, actuators, sensors):
        self.mind = mind
        #self.__name__ = name #ID IS ALREADY PART OF THE AGENT  - Identifiable
        if isinstance(actuators, dict) or isinstance(actuators, list) or isinstance(actuators, tuple):
            self._actuators = actuators
            if isinstance(actuators, dict):
                self.actuators = lambda : list(self._actuators.values())
            else:
                self.actuators = lambda : self._actuators
            for a in self.actuators():
                a.owner = self.ID
        else:
            raise ValueError("actuators must be a dict, list or tuple")
        if isinstance(sensors, dict) or isinstance(sensors, list) or isinstance(sensors, tuple):
            self._sensors = sensors
            if isinstance(sensors, dict):
                self.sensors = lambda : list(self._sensors.values())
            else:
                self.sensors = lambda : self._sensors

            for s in self.sensors():
                s.owner = self.ID
        else:
            raise ValueError("sensors must be a dict, list or tuple")
            
        self.mind.__post_init__(self)
        
    def find_actuators(self, action):
        return self.find(action, self.actuators())
        
    def find_sensors(self, perception):
        return self.find(perception, self.sensors())
    
    def find(self, event, collection):
        return [arg for arg in collection if type(event) in arg.subscribe]
                    
    def cycle(self):
        return self.mind.cycle()
    
    def __hash__(self):
        return self.ID.__hash__()
        
    def __eq__(self):
        return self.ID.__eq__()

class Actuator(Identifiable, Transient):
  
    def __init__(self):
        super(Actuator, self).__init__()
        self.owner = None
        
    def attempt(self, action):
        action.__post_init__(self.owner)
        super(Actuator, self).sink(action)

class Sensor(Identifiable, Transient):
    
    def __init__(self):
       super(Sensor, self).__init__()
       self.owner = None

    def notify(self, perception):
        super(Sensor, self).sink(perception)