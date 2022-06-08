class myclass:
    x =5

p1 = myclass()
print(p1.x)

######################################################

class person:
    def __init__(self , name , age):
        self.name = name
        self.age = age 

p1 = person("tlqkf" , 18)

print(p1.name)
print(p1.age) # init의 활용방법

#######################################################

class person:
    def __init__(self, name , age ):
        self.name = name    
        self.age = age 
    def myfunc(self):
        return "안녕하세요" + str(self.age) + "살" + self.name + "님"

p1 = person("tlqkf",18)
print(p1.myfunc())  # 클래스 내의 함수를 쓸때에는 ()를 붙여주어야 함 

########################################################

class Person:
    def __init__(self , name):
        self.firstname = name

    def printname(self):
        print(self.firstname)
    
class student(Person):
    pass

x = student("dbwofla")
x.printname() # x에 부여한 student 부모클래스의 메서드 호출 

##########################################################


