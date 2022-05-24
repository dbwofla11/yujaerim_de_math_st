# GUI 계산기 인터페이스 만들기 
 # Lab10 - 1 텍스트로 계산기 만들기 
from tkinter import *


#모듈 정의 
def add():
    result = '출력 : ' + str(float(entryA.get()) + float(entryB.get()))
    print(result)
    labRst.configure(text = result )

def minus():
    result = '출력 : ' + str(float(entryA.get()) - float(entryB.get()))
    print(result)
    labRst.configure(text = result )

def mul():
    result = '출력 : ' + str(float(entryA.get()) * float(entryB.get()))
    print(result)
    labRst.configure(text = result )

def div():
    result = '출력 : ' + str(float(entryA.get()) / float(entryB.get()))
    print(result)
    labRst.configure(text = result )

def double_mul():
    result = '출력 : ' + str(float(entryA.get()) ** float(entryB.get()))
    print(result)
    labRst.configure(text = result )


tk = Tk()
tk.title("계산기 예제 TEXT버전 LAB_10")
tk.geometry("500x50")


Label(tk, text="입력: A " , width=5).pack(side=LEFT)

#텍스트 박스 정의 1
entryA = Entry(tk , width=5)
entryA.insert(0,'0')
entryA.pack(side=LEFT)

Label(tk, text="입력: B " , width=5 ).pack(side=LEFT)

entryB = Entry(tk , width=5)
entryB.insert(0,'0')
entryB.pack(side=LEFT)

Label(tk, text="연산 :  " , width=5 ).pack(side=LEFT)

#버튼 정의 코딩 
btnAdd = Button(tk, text="+", width=3 , command=add)
btnAdd.pack(side=LEFT)

btnminus = Button(tk, text="-" , width=3 , command=minus)
btnminus.pack(side=LEFT) 

btnmul = Button(tk, text="*" , width=3 , command=mul)
btnmul.pack(side=LEFT) 

btndiv = Button(tk, text="/" , width=3 , command=div)
btndiv.pack(side=LEFT) 

btndouble = Button(tk, text="**" , width=3 , command=double_mul)
btndouble.pack(side=LEFT) 

labRst = Label(tk , text="출력 : 0.0" , width=20 ,  anchor = "w")
labRst.pack(side=LEFT)

tk.mainloop()