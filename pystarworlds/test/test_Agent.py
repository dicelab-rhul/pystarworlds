from pystarworlds.Agent import Body, Sensor, Actuator, Mind, new_actuator, new_sensor



if __name__ == "__main__":

    def actuator_test1():
        a1 = Actuator()
        a2 = Actuator()
        a3 = Actuator()

        b = Body(None, [a1,a2], [])    
        print(b.actuators)
        print(b.sensors)
        for a in b.actuators:
            print(a.body)
        
        b.add_actuator(a3)
        print(b.actuators)
        #b.add_actuator(a1) #error!
  
    def actuator_test2():
        a1_cls = new_actuator('actuator1')
        a2_cls = new_actuator('actuator2', 'a1', 'a2', t1=0)
        print(a1_cls().subscribed)
        print(a2_cls().subscribed)

    actuator_test2()

