#커스텀으로 GUI디자인 만들기
import os 
from tkinter import *

tk = Tk()
tk.title("임시 커스텀 메모장 GUI ")
tk.geometry("640x480")

# 열기 , 저장 파일 이름 
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): # 파일 있으면 1 아니면 0  
        with open(filename, "r" , encoding="utf-8") as file:
            txt.insert(END , file.read())

def save_file():
    with open(filename, "w" , encoding="utf-8") as file:
        file.write(txt.get("1.0" , END))

menu = Menu(tk)
menu_file = Menu(menu , tearoff=0)
menu_file.add_command(label="열기" ,command=open_file)
menu_file.add_command(label="저장" ,command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기" , command=tk.quit)
menu.add_cascade(label="파일" , menu=menu_file)

# 편집 , 서식 , 보기 ,도움말 
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤 바 
scrollbar = Scrollbar(tk)
scrollbar.pack(side="right" , fill="y")

# 본문영역 
txt = Text(tk , yscrollcommand=scrollbar.set)
txt.pack(side="left" , fill="both" , expand=True)
scrollbar.config(command=txt.yview)

tk.config(menu=menu)
tk.mainloop()