
from BasicBuildingBlock.Event import Event

class Perception(Event):
    
    def __init__(self,ownerid):
        super().__init__()
        self.owner_id=ownerid
        
    def execute(self, ambient):
        return []
    def getOwner(self):
        return self.owner_id
    def setOwner(self,ownerid):        # Retrieves the sensor's associated agent
       self.owner_id=ownerid
    def __str__(self):
        return super().__str__() 
    
    
