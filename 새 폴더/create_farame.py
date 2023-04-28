# GUI(Graphic User Interface) Programming - TKInter

from tkinter import *

root = Tk()
root.title("Tk Test") # 제목
#root.geometry("640x480") # 가로, 세로
root.geometry("640x480+800+200") # x좌표, y좌표
root.resizable(True, False) # widht, height # 창 크기 조정

# Button
# btn1 = Button(root, text='버튼1')
# btn1.pack()

# btn2 = Button(root, padx=5, pady=10, text='버튼2')
# btn2.pack()

# btn3 = Button(root, padx=10, pady=5, text='버튼3')
# btn3.pack()

# btn4 = Button(root, width=10, height=3, text='버튼4')
# btn4.pack()

# btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
# btn5.pack()

# photo = PhotoImage(file="./img.png")
# btn6 = Button(root, image=photo)
# btn6.pack()

# def btncmd():
#     print("버튼이 클릭되었어요.")

# btn7 = Button(root, text="동작하는 버튼", command=btncmd)
# btn7.pack()

# Label
# label1 = Label(root, text="안녕하세요")
# label1.pack()

# photo = PhotoImage(file="./img.png")
# label2 = Label(root, image=photo)
# label2.pack()

# def change():
#     label1.config(text='또 만나요')
    
#     global photo2
#     photo2 = PhotoImage(file="./img2.png")
#     label2.config(image=photo2)

# btn1 = Button(root, text="클릭", command=change)
# btn1.pack()

# Text
# txt = Text(root, width=30, height=5)
# txt.pack()
# txt.insert(END, "글자를 입력하세요.")

# # Entry
# e = Entry(root, width=30)
# e.pack()
# e.insert(0, "한 줄만 입력하세요.")

# def btncmd():
#     # 내용 출력
#     print(txt.get("1.0", END)) # 1 - 첫 번째 라인, 0 - 0번째 Column위치
#     print(e.get())
    
#     # 내용 삭제
#     txt.delete("1.0", END)
#     e.delete(0, END)

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

# Listbox
# listbox = Listbox(root, selectmode="extended", height=0) # extended = 2개 이상의 리스트를 선택
# listbox.insert(0, "사과")
# listbox.insert(1, "딸기")
# listbox.insert(2, "바나나")
# listbox.insert(END, "수박") # END - 리스트의 맨 마지막에 위치
# listbox.insert(END, "포도")
# listbox.pack()

# def btncmd():
#     # 삭제
#     listbox.delete(0) # 맨 앞 항목을 삭제
    
#     # 갯수 확인 
#     print("이 리스트에는", listbox.size(), "개가 있어요.")
    
#     # 항목 확인 (시작 index, 끝 index)
#     print("3번째까지의 항목 : ", listbox.get(0, 2))    

# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

# Checkbox
# chkvar = IntVar() # chkvar에 Int형으로 값을 저장한다.
# chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable=chkvar)
# chkbox.select() # 자동 선택 # .deselect() - 선택 해제
# chkbox.pack()

# chkvar2 = IntVar() # chkvar에 Int형으로 값을 저장한다.
# chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable=chkvar2)
# chkbox2.pack()

# def btncmd():
#     print(chkvar.get())
#     print(chkvar2.get()) # 0: 체크 해제, 1 : 체크
    
# btn = Button(root, text="클릭", command=btncmd)
# btn.pack()

# RadioButton - 한 번에 하나만 선택

# Label(root, text="메뉴를 선택하세요.").pack()
# # label1 = Label(root, text="메뉴를 선택하세요.")
# # label1.pack()

# burger_var = IntVar() # Int 형으로 값을 저장한다.
# btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var )
# btn_burger1.select() # 기본값 선택
# btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var )
# btn_burger3 = Radiobutton(root, text="싸이버거", value=3,  variable=burger_var)
# btn_burger1.pack()
# btn_burger2.pack()
# btn_burger3.pack()

# Label(root, text="음료를 선택하세요.").pack()
# # label1 = Label(root, text="메뉴를 선택하세요.")
# # label1.pack()

# drink_var = StringVar() # String 형으로 값을 저장한다.
# btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var )
# btn_drink1.select() # 기본값 선택
# btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var )
# btn_drink3 = Radiobutton(root, text="커피", value="커피",  variable=drink_var)
# btn_drink1.pack()
# btn_drink2.pack()
# btn_drink3.pack()

# def btncmd():
#     print(burger_var.get())
#     print(drink_var.get())
    
# btn = Button(root, text="주문하기", command=btncmd)
# btn.pack()







root.mainloop()