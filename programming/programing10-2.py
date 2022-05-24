#은행계좌 클래스 및 클래스 상속 
# Bank클래스 선언 
class Bank:
    def __init__(self , name , number , balance ):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    def deposit(self , amount):
        self.balance += amount
        return self.balance
#아들 클래스 save 선언
class save(Bank):
    def __init__(self, name, number, balance , in_rate):
        super().__init__(name, number, balance)
        self.in_rate = in_rate
    def set_in_rate(self , in_rate):
        self.in_rate = in_rate
    def get_in_rate(self):
        return self.in_rate
    def add_in_rate(self):
        self.balance += self.balance*self.in_rate
#아들 클래스 check클래스 선언
class check(Bank):
    def __init__(self, name, number, balance):
        super().__init__(name, number, balance)
        self.withdraw_charge = 10000 # 이게 수표발행할때의 수수료
    def withdraw(self, amount):
        return Bank.withdraw(self , amount + self.withdraw_charge)
print("은행계좌 클래스 및 상속 ")
a1 = save("홍길동" , 123456 , 100000, 0.2)
a1.add_in_rate()
print("저축예금의 잔액=",a1.balance)
a2 = check("김철수",111222333, 2000000)
a2.withdraw(100000)
print("당좌예금의 잔액 =",a2.balance)