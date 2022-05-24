'''
def factre(n):
    if(n ==1 ): return 1
    return n * factre(n-1)

print(factre(4))

'''
#클래스 기반 
'''
class student:
    def __init__(self, name , kr , eng , mt , science):
        self.name = name
        self.kr = kr 
        self.mt = mt 
        self.science = science
        self.eng = eng

    def get_sum(self):
        return self.kr + self.mt + self.eng + self.science
    
    def get_avg(self):
        return self.get_sum() / 4
    
    def string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())

students = [student("윤인성", 39 , 92 , 89 , 90),
student("유재림", 123, 123,32, 232),
student("백승민" , 123 ,122, 333,232) ,
student("ssss",123,123,123,111)]

print("클래스 기반 성적 처리 ")
print("이름", "총점" , "평균" , sep = "\t")

for student in students:
    print(student.string())
'''
'''
#딕셔너리 기반 

def student(name , kr , mt , eng , sc):
    return {"name":name,"kr":kr,"mt":mt,"eng":eng,"sc":sc}

def get_sum(student):
    return student["kr"] + student["mt"] + student["eng"] + student["sc"]

def average(student):
    return get_sum(student) /4

def string(student):
    return "{}\t{}\t{}".format(student["name"], get_sum(student) , average(student))

students = [student("윤인성", 39 , 92 , 89 , 90),
student("유재림", 123, 123,32, 232),
student("백승민" , 123 ,122, 333,232) ,
student("ssss",123,123,123,111)]

print("딕션너리 기반 처리")

for i in students:
    print(string(i))
    '''
'''
#Lab 7-2
class friend:
    def __init__(self, name , phone):
        self.name = name
        self.phone = phone
    def get_name(self):
        return self.name
    def get_phone(self):
        return self.phone
    def set_phone(self , phone):
        self.phone = phone
    def show(self):
        print("이름 : ",self.name)
        print("연락처 : ", self.phone)
print("클래스 기반 연락처 관리 ")
f = friend("유재림" , "010-3674-6070")
f.get_name()
f.get_phone()
f.set_phone("010-3674-0000")
f.show()
frs = []
frs.append(friend("백승민", "010-3030-3333"))
frs.append(friend("aaa","111-222-333"))
frs.append(friend("유시민","111-222-3333"))

for i in frs:
    i.show()

print("유씨 성을 가진 사람의 연락처 출력")
for i in frs:
    if i.get_name().startswith('유'):
        i.show()

#백승민의 전화번호 수정 
for i in frs:
    if i.get_name() == "백승민":
        i.set_phone("010-111-222")
#친구 정보 출력 
for i in frs:
    if i.get_name() == "백승민":
        i.show()

'''

#Lab 7-3
print("class 기반의 은행계좌 코드 만들기")
class bank:
    def __init__(self):
        self.balance = 0
    def out(self, amount):
        self.balance -= amount
        print("통장에 {}원이 출금되었습니다".format(amount))
        return self.balance
    def inbank(self , amount):
        self.balance += amount
        print("통장에 {}원이 입금되었습니다".format(amount))
        return self.balance

a = bank()
a.inbank(1000)
a.out(400)

print("class 기반의 자동차만들기 코드")
class car:
    def __init__(self , speed = 0 , gear = 1 , color = "white"):
        self.speed = speed
        self.gear = gear
        self.color = color
    def setspeed(self,speed):
        self.speed = speed 
    def setgear(self,gear):
        self.gear = gear
    def setcolor(self,color):
        self.color = color
    
    def string(self):
        return "{}\t{}\t{}" .format(self.speed , self.gear , self.color)
    
mycar = car()
mycar.setgear(3)
mycar.setcolor("black")
mycar.setspeed(100)
print(mycar.string())
