"""
@author Benedict Wilkins
@author: Nausheen Saba Shahid
"""

class Identifiable:    #Identifiable is inherited from ABC
         
    def SimpleIDGenerator():  # Unique Id generator
        i = 0
        while(True):
            yield str(i)
            i += 1
    
    IDGEN = SimpleIDGenerator()
    
    def __new__(cls, *args, **kwargs):
        #print("NEW", *args, **kwargs)
        obj = super(Identifiable, cls).__new__(cls)
        obj.__ID = next(Identifiable.IDGEN)
        return obj
    
    def __str__(self):       # equvilent to tostring
        return self.__class__.__name__ + "@" + self.ID

    @property
    def ID(self):
        return self.__ID
    
    def __unicode__(self):
        return self.__str__()
    
    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.ID.__hash__()
        
    def __eq__(self):
        return self.ID.__eq__()
