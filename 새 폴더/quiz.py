# 연습 문제

# 메모장 프로그램 만들기
# 1. 제목 : 제목 없음 - Windows 메모장
# 2. 크기 : 640*480(가로, 세로 크기 조정이 가능하도록)
# 3. 파일 메뉴 생성
#    새 파일
#    열기
#    저장
#    끝내기
# 4. 그 외 편집, 서식, 보기, 도움말 메뉴를 생성
#  편집 메뉴에서 잘라내기, 복사 메뉴를 생성 후 복사 메뉴는 비활성화
#  보기 메뉴에서 확대/축소하기, 상태표시줄 선택할 수 있도록 설정
# 5. 아래쪽 상태바는 생성 안함
# 6. 스크롤바를 오른쪽으로


import os
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") # 가로 * 세로

filename = "mynote.txt"
def open_file():
    if os.path.isfile(filename): # 경로에 파일이 있으면 True, 없으면 False
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, file.read()) # 파일 내용에 본문 내용에 입력
            
def save_file():
    with open(filename, "w", encoding="utf-8") as file:
        file.write(txt.get("1.0", END)) # 모든 내용을 가져와서 저장
    
    
    
    
# 메뉴 부분
menu = Menu(root)
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="새 파일")
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)

# 편집, 서식, 보기, 도움말
menu_edit = Menu(menu, tearoff=0)
menu_edit.add_command(label="잘라내기")
menu_edit.add_command(label="복사", state="disabled")
menu.add_cascade(label="편집", menu=menu_edit)

menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 본문 영역
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()