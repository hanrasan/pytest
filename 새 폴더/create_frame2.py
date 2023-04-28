from tkinter import *
import tkinter.ttk as ttk
import time

root = Tk()
root.title("TP2 Test")
root.geometry("640x480")

# values = [str(i) + "일" for i in range(1, 32)] # 1~31까지의 숫자
# combobox = ttk.Combobox(root, height=5, values=values)
# combobox.pack()
# combobox.set("카드 결제일") # 최초 제목 목록 설정

# readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # 읽기 전용
# readonly_combobox.pack()
# readonly_combobox.current(0) # 0번째 인덱스 값 선택

# def btncmd():
#     print(combobox.get())
#     print(readonly_combobox.get())
    
# btn = Button(root, text="선택", command=btncmd)
# btn.pack()

# Progressbar 
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(5) # 5ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 작동 중지
    
# btn = Button(root, text="중지", command=btncmd)
# btn.pack()

# p_var2 = DoubleVar()
# progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
# progressbar2.pack()

# def btncmd2():
#     for i in range(1, 101):
#         time.sleep(0.01)
        
#         p_var2.set(i)
#         progressbar2.update()
#         print(p_var2.get())
    
# Menu
# File 메뉴

def create_new_file():
    print("새 파일을 만듭니다.")
    
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)    
menu_file.add_command(label="New File", command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File")
menu_file.add_separator()
menu_file.add_command(label="Save File", state="disabled") # 비활성화
menu_file.add_command(label="exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

menu.add_cascade(label="Edit")

menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu.add_cascade(label="Language", menu=menu_lang)

menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu_view.add_checkbutton(label="++ View")
menu.add_cascade(label="View", menu=menu_view)
    
# btn = Button(root, text="시작", command=btncmd2)
# btn.pack()


root.config(menu=menu)
root.mainloop()