"""
@author: Nausheen Saba Shahid
"""
from .Event import Event

class Action(Event):
    
    def __init__(self, actor):
        super(Action, self).__init__()
        self.__actor__ = actor
        
