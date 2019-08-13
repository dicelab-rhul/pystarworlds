"""
@author: Nausheen Saba Shahid
"""


from abc import ABC

class Identifiable(ABC):    #Identifiable is inherited from ABC
         
    def SimpleIDGenerator():  # Unique Id generator
        i = 0
        while(True):
            val = yield    
            yield val + str(i)
            i += 1
    
    IDGEN = SimpleIDGenerator()
    
    def __new__(typ, *args, **kwargs):   # new cannot be overrided by any sub class
        obj = super(Identifiable, typ).__new__(typ)
        next(Identifiable.IDGEN)
        obj.ID = Identifiable.IDGEN.send("@") #+ obj.__class__.__name__)
        return obj
    
    def __str__(self):       # equvilent to tostring
        return self.__class__.__name__ + self.ID
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()
    
