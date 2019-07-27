"""
@author: Nausheen Saba Shahid
"""


# class for event
# class for source of event
from abc import  abstractmethod
from .Identifiable import Identifiable

class Source:
    
    def __iter__(self):
        return self
    
    def __next__(self):
        return self.source()
        
    @abstractmethod
    def source(self):
        pass
   
    # class for sink of event

class Sink:
    
    def __init__(self, buffer):
        self.buffer = buffer
    
    def sink(self, event):
        assert type(event) in type(self).subscribe
        self.buffer.append(event)
  
    # class for buffer of event
  
    
class Transient(Source, Sink):
    
    def __init__(self):
        Sink.__init__(self, [])
        Source.__init__(self)

    def __len__(self):
        return len(self.buffer)
    
    def __next__(self):
        if(len(self.buffer) == 0):
            raise StopIteration
        return self.source()
    
    def source(self):
       return self.buffer.pop()
    
    def sink(self, event):
        self.buffer.append(event)
        
    def setEmpty(self):
       self.buffer =[]
      
    def isEmpty(self):
        if(len(self.buffer)):
         return False
        else: 
         return True
     
class Event(Identifiable):
    
    def __init__(self):
        pass 
    
class Perception(Event):
    
    def __init__(self):
        super(Perception, self).__init__()
        
class Action(Event):
    
    def __init__(self):
        super(Action, self).__init__()
        self.__actor__ = None
        
    def __post_init__(self, actor):
        self.__actor__ = actor
        
class Executor:
    
    def __init__(self, _type):
        self._type = _type
        
    def __call__(self, env, action):
        pass
    
      