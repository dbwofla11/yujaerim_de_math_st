#클래스 상속 
#상속은 어떤 클래스를 기반으로 그 속성과 기능을 물려받는거 
class car:
    def __init__(self , speed):
        self.speed = speed
    def setspeed(self , speed):
        self.speed = speed
    def getdesc(self):
        return "차량 = ("+str(self.speed) + ")" 

class spcar(car):
    def __init__(self, speed , turbo):
        super().__init__(speed)
        self.turbo = turbo
    def setturbo(self , turbo):
        self.turbo = turbo

print("(1)car 클래스 상속에 의한 spcar클래스 생성 ")
obj = spcar(100 , True)
print(obj.getdesc())
obj.setturbo(False)