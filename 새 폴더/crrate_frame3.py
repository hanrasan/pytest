from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()
root.title("TP2 Test")
root.geometry("640x480")

# 기차 예매 시스템이라고 가정
# def info():
#     msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")
    
# def warn():
#     msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

# def error():
#     msgbox.showerror("에러", "결제 오류가 발생했습니다.")
    
# def okcancel():
#     msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    
# def retrycancle():
#     msgbox.askretrycancel("재시도 / 취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
    
# def yesno():
#     msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향입니다. 예매하시겠습니까?")
    
# def yesnocancel():
#     response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다.\n저장 후 다시 하세요")
#     print("응답 :", response)
    
#     if response == 1 :
#         print("예")
#     elif response == 0:
#         print("아니오")
#     else:
#         print("취소")
    
# Button(root, command=info, text = "알림").pack()
# Button(root, command=warn, text = "경고").pack()
# Button(root, command=error, text = "에러").pack()

# Button(root, command=okcancel, text = "확인 취소").pack()
# Button(root, command=retrycancle, text = "재시도 취소").pack()
# Button(root, command=yesno, text = "예 아니오").pack()
# Button(root, command=yesnocancel, text = "예 아니오 취소").pack()

# Frame
# Label(root, text="메뉴를 선택하세요.").pack(side="top")

# # 메뉴 프레임
# frame_burger = Frame(root, relief = "solid", bd=1)
# frame_burger.pack(side="left", fill="both", expand=True)

# Button(frame_burger, text="햄버거").pack()
# Button(frame_burger, text="치즈햄버거").pack()

# # 음료 프레임
# Label(root, text="음료를 선택하세요.").pack(side="bottom")
# frame_drnik = LabelFrame(root, text='음료')
# frame_drnik.pack(side="right", fill="both", expand=True)
# Button(frame_drnik, text="콜라").pack()
# Button(frame_drnik, text="사이다").pack()

# Scrollbar

# frame = Frame(root)
# frame.pack()

# scrollbar = Scrollbar(frame)
# scrollbar.pack(side="right", fill="y")

# # set이 없으면 스크롤을 내려도 다시 올라옴
# listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)
# for i in range(1, 32):
#     listbox.insert(END, str(i) + "일")
# listbox.pack(side="left")

# scrollbar.config(command=listbox.yview)


# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")
# btn1.pack(side="left")
# btn2.pack(side="right")

# btn1.grid(row=0, column=0)
# btn1.grid(row=1, column=1)
# btn1.pack()
# btn2.pack()

# 키보드 맨 윗줄
btn_num = Button(root, text="Num", width=5, height=2, padx=3, pady=3)
btn_slash = Button(root, text="/", width=5, height=2, padx=3, pady=3)
btn_as = Button(root, text="*", width=5, height=2)

btn_num.grid(row=0, column=0,)
btn_slash.grid(row=0, column=1)
btn_as.grid(row=0, column=2)

btn_7 = Button(root, text="7", width=5, height=2, padx=3, pady=3)
btn_8 = Button(root, text="8", width=5, height=2, padx=3, pady=3)
btn_9 = Button(root, text="9", width=5, height=2, padx=3, pady=3)

btn_7.grid(row=1, column=0,)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)

btn_0 = Button(root, text="0", width=5, height=2) # 가로로 합쳐짐
btn_point = Button(root, text="Del", width=5, height=2)

# columnspan -> 가로로 몇 칸 합칠지, rowspan -> 세로호 몇 칸 합칠지
btn_0.grid(row = 2, column=0, columnspan=2, padx=3, pady=3, sticky=N+E+W+S)
btn_point.grid(row=2, column=2, padx=3, pady=2)

root.mainloop()
