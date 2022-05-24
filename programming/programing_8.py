#프로그래밍 실습 

class cat:
  def __init__(self , name = None , age = 0):
    self.name = name
    self.age = age
  def Inform(self):
    return self.name , self.age

c = cat("asdasdasd",cnt)
s = cat("aaaa",cnt)
print(c.Inform())
print(s.Inform())

