#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    Created on 20-11-2020 15:22:52

    [Description]
"""
__author__ = "Benedict Wilkins, Nausheen Saba Shahid"
__email__ = "benrjw@gmail.com"
__status__ = "Development"

from abc import  abstractmethod
from ..common import Identifiable

class Source:
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.source()
        
    @abstractmethod
    def source(self):
        pass
    
class Sink:
    
    def __init__(self):
        pass 
    
    def sink(self, event):
        #assert type(event) in type(self).subscribe TODO use in a decorator in all subclasses? 
        pass 

class Transient(Source, Sink):
    
    def __init__(self):
        Sink.__init__(self)
        Source.__init__(self)
        self.buffer = []

    def __len__(self):
        return len(self.buffer)
    
    def __next__(self):
        if not self.isEmpty():
            return self.source()
        raise StopIteration()
    
    def source(self):
       return self.buffer.pop()
    
    def sink(self, event):
        self.buffer.append(event)

    def clear(self):
       self.buffer.clear()
      
    def isEmpty(self):
        return not bool(len(self.buffer))

class Event(Identifiable):
    
    def __init__(self, source=None):
        super(Event, self).__init__()
        self.__source = source

    @property
    def source(self):
        if self.__source is None:
            raise ValueError("Event '{0}' has no source, did you forget to set the source?")
        return self.__source 

    @source.setter
    def source(self, value):
        if self.__source is None:
            self.__source = value
        else:
            raise ValueError("Cannot re-set source of event {0}".format(self.ID))
    
class Perception(Event):
    
    def __init__(self):
        super(Perception, self).__init__()

class Action(Event):
    
    def __init__(self):
        super(Action, self).__init__()
        
class Executor:
    
    def __init__(self, _type):
        self._type = _type
        
    def __call__(self, env, action):
        pass
    
# ======================================================== #
# ====================== FACTORY ========================= #
# ======================================================== #

def new_action(name, *data, base_type=(Action,)):
    return type(name, base_type, {'data':data}) #dynamically creates a new action class
