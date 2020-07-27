"""
@author: Nausheen Saba Shahid
@author: Benedict Wilkins
"""

#from ABC import abstractmethod

from collections import UserDict

from .Identifiable import Identifiable
from .Event import Transient

class InternalAgentError(Exception):
    pass

# ==================== CLASSES ==================== #

class BodyComponent(Identifiable):
    
    def __init__(self, *args, **kwargs):
        super(BodyComponent, self).__init__(*args, **kwargs)        
        self.__body = None
    
    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        self.__body = value

class ComponentDict(UserDict):
    '''
        A custom dictionary that allows a user to easily add new 
        actuators/sensors. Adding/removing a new component has some side 
        effects - most notably assigning a body to the component.
    '''

    def __init__(self, body):
        super(ComponentDict, self).__init__()
        self.__body = body

    def subscribed(self, key): #TODO make more efficient?
        return {k:v for k,v in self.items() if key in v.subscribe}

    def __delitem__(self, key):
        value = self[key]
        super().__delitem__(key)
        value._BodyComponent__body = None
    
    def __setitem__(self, key, value):
        if key in self:
            raise InternalAgentError("Cannot add duplicate {0} to {1}".format(str(value), str(self.__body)))
        
        super().__setitem__(key, value)
        value._BodyComponent__body = self.__body

# ==================== API ==================== #

class Mind(BodyComponent):

    def __init__(self, *args, **kwargs):
        super(Mind, self).__init__(*args, **kwargs)

    def cycle(self): #TODO make abstract
        pass

class Actuator(BodyComponent, Transient):

    __actions__ = []
  
    def __init__(self, *args, **kwargs):
        super(Actuator, self).__init__(*args, **kwargs)
        
    def attempt(self, action):
        action.source = self.body.ID
        super(Actuator, self).sink(action)

class Sensor(BodyComponent, Transient):

    __perceptions__ = []
    
    def __init__(self, *args, **kwargs):
       super(Sensor, self).__init__(*args, **kwargs)

    def notify(self, perception):
        super(Sensor, self).sink(perception)
    
    @property
    def valid_perceptions(self):
        return self.__class__.__perceptions__

class Body(Identifiable):
    
    def __init__(self, mind, actuators=[], sensors=[]):
        super(Body, self).__init__()
        self.__actuators = ComponentDict(self)
        self.__sensors = ComponentDict(self)
        self.__actuators.update({a.ID:a for a in actuators})
        self.__sensors.update({s.ID:s for s in sensors})

        self.mind = mind
    
    @property
    def actuators(self):
        return self.__actuators

    @property
    def sensors(self):
        return self.__sensors

    def add_actuator(self, actuator, name=None):
        if name is None:
            name = actuator.ID
        self.__actuators[name] = actuator
    
    def add_sensor(self, sensor, name=None):
        if name is None:
            name = sensor.ID
        self.__sensors[name] = sensor

    @property
    def mind(self):
        return self.__mind

    @mind.setter
    def mind(self, value):
        self.__mind = value
        self.__mind.body = self

    def __str__(self):
        return "{0}({1}: {2} | {3})".format(super().__str__(), self.mind, self.sensors, self.actuators)

    def attempt(self, **actions):
        '''
            Attempts all of the actions specified by the actions dictionary.
            The actions dictionary consists of actuator (ID) keys and action (Event) values.
        '''
        try:
            for actuator, action in actions.items():
                if action is not None:
                    self.__actuators[actuator].attempt(action)
        except KeyError as e:
            pass #TODO raise InternalAgent Error
    
    def perceive(self, key=None):
        '''
            Get all current perceptions from sensors.
            Parameters:
                key: 

            Returns:
                percepts (dict): {sensor_name:[percept1, percept2], ...}
        '''
        perceptions = {}
        if key is None: #get all perceptions for all sensors
            for name, sensor in self.__sensors.items():
                perceptions[name] = [p for p in sensor]
        else:
            for name, sensor in self.__sensors.subscribed(key).items():
                perceptions[name] = [p for p in sensor]
        return perceptions


    def cycle(self):
        return self.mind.cycle()

# ======================================================== #
# ====================== FACTORY ========================= #
# ======================================================== #

def new_actuator(name, *actions, base_type=(Actuator,), **data):
    a_cls = type(name, base_type, data)
    a_cls.__actions__ = actions #no need for a meta class?
    a_cls.subscribe = property(lambda self: self.__actions__)
    return a_cls

def new_sensor(name, *perceptions, base_type=(Sensor,), **data):
    s_cls = type(name, base_type, data)
    s_cls.__perceptions__ = perceptions
    s_cls.subscribe = property(lambda self: self.__perceptions__)
    return s_cls