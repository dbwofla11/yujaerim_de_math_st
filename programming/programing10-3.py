class car:
    def __init__(self , speed):
        self.speed = speed
    def setspeed(self , speed):
        self.speed = speed
class Truck(car):
    def __init__(self, speed , payload):
        super().__init__(speed)
        self.payload = payload
    def setpayload(self , payload):
        self.payload = payload
    def getpayload(self):
        return "탑재량 = ("+str(self.payload)+ ")"
class Bus(car):
    def __init__(self, speed , ns):
        super().__init__(speed)
        self.ns = ns
    def setNumseats(self, ns):
        self.ns = ns
    def getNumSeats(self):
        return "탑승객 수 = ("+str(self.ns)+ ")"

print("탈것 클래스 및 상속")
a1 = Truck(100,5000)
a1.setpayload(5000)
print(a1.getpayload())
b1 = Bus(90,30)
b1.setNumseats(30)
print(b1.getNumSeats())




