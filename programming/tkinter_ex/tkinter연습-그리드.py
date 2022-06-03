from tkinter import *

# 함수선언 

root = Tk() # tkinter 시작하기 
# 여기에다 GUI코딩

lb1 = Label(root , text="이름")
lb1.grid(row=0 , column=0)

txt = Entry(root)
txt.grid(row=0 , column=1) # 행렬로 배치 

btn1 = Button(root , text="start" , width=20)
btn1.grid(row=1,column=1)

root.mainloop() # tkinter 마무리 짓기 







