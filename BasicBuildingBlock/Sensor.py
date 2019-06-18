from BasicBuildingBlock.Identificaiton import Identifiable
from BasicBuildingBlock.Event import Transient

class Sensor(Identifiable,Transient):
    
  def __init__(self):
   super().__init__()
   self.isSensing=True;
   
  def notifyEvent(self,event):
  #  if(super().isEmpty()):  
      super().sink(event)
  
  def getPercepion(self):
    perceptionList=[] 
    while(super().isEmpty()==False):
      perceptionList.append(super().source())   
    return perceptionList

  def startSensing():   # Start the sensing process
    self.isSensing=True;
  def stopSensing():   # Stop the sensing process
    self.isSensing=False;
  def isSensing():   #  Whether sensor is sensing or not
    return self.isSensing;
  def setDevice(device):   # Set the sensor to an input device
    pass
  def getDevice():        # Retrieves the sensor's associated input device
    pass  
  def getLastTime():       # Returns the time associated with the most recent sensor reading.
    pass
  def getLastReading():   # Returns the most recent sensor reading
    pass
  def getSensorSubscribedCount():
    pass
  def getRange():   # Retus thee range max-min possible values
    pass
  def getMeasuringUnit():   # Returns thee measuring unit of reading
    return " "

 
  def getOwner(self):        # Retrieves the sensor's associated agent
    return self.agent_id
 
  def setOwner(self,ag1):        # Retrieves the sensor's associated agent
    self.agent_id=ag1
 
  def isEmpty(self):
    return super().isEmpty()
  
    
