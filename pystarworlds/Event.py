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
    
    @abstractmethod
    def sink(self, event):
        pass
  
    # class for buffer of event
  
    
class Transient(Source, Sink):
    
    def __init__(self):
       self.buffer =[]
        
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
      