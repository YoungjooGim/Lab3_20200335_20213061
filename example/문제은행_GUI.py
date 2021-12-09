import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("열혈파이썬 기초편 연습문제")
#root.resizable(False, False)


# 다음 버튼  /  btn_combobox_chapters
def practices():
    if combobox_chapters.get() == "Chapter1":
        combobox_practices['values'] = ["연습문제01-1", "연습문제01-2", "연습문제01-3"]
        combobox_practices.set("Chapter1")
    elif combobox_chapters.get() == "Chapter2":
        combobox_practices['values'] = ["연습문제02-1", "연습문제02-2", "연습문제02-3"]
        combobox_practices.set("Chapter2")
    elif combobox_chapters.get() == "Chapter3":
        combobox_practices['values'] = ["연습문제03-1", "연습문제03-2", "연습문제03-3", "연습문제03-4"]
        combobox_practices.set("Chapter3")   
    else:
        combobox_practices.set("PRESS 다음")

# 문제풀이시작 버튼  /   btn_combobox_practices

notebook = ttk.Notebook(root)  
def start_solving():   
    global notebook
    if combobox_chapters.get() == "Chapter1" and combobox_practices.get() == "연습문제01-1":
        
        new_notebook = Q01_1
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    elif combobox_chapters.get() == "Chapter1" and combobox_practices.get() == "연습문제01-2":
        
        new_notebook = Q01_2
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    elif combobox_chapters.get() == "Chapter1" and combobox_practices.get() == "연습문제01-3":
        
        new_notebook = Q01_3
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")

    elif combobox_chapters.get() == "Chapter2" and combobox_practices.get() == "연습문제02-1":
        
        new_notebook = Q02_1
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    
    elif combobox_chapters.get() == "Chapter2" and combobox_practices.get() == "연습문제02-2":
        
        new_notebook = Q02_2
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    
    elif combobox_chapters.get() == "Chapter2" and combobox_practices.get() == "연습문제02-3":
        
        new_notebook = Q02_3
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    
    elif combobox_chapters.get() == "Chapter3" and combobox_practices.get() == "연습문제03-1":
        
        new_notebook = Q03_1
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    
    elif combobox_chapters.get() == "Chapter3" and combobox_practices.get() == "연습문제03-2":
        
        new_notebook = Q03_2
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")
    
    elif combobox_chapters.get() == "Chapter3" and combobox_practices.get() == "연습문제03-3":
        
        new_notebook = Q03_3
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")

    elif combobox_chapters.get() == "Chapter3" and combobox_practices.get() == "연습문제03-4":
        
        new_notebook = Q03_4
        notebook.destroy()
        notebook = new_notebook
        notebook.pack(fill="both")

    else: pass


##정답버튼

#연습문제 01_1
def A01_1_Q1():
    lbl_A01_1_frame1.config(text=">>> print(\"윤성우\")\n윤성우")
    print(lbl_A01_1_frame1.cget("text"))

def A01_1_Q2():
    lbl_A01_1_frame2.config(text=">>> 1+2+3+4+5+6+7+8+9+10\n55")
    print(lbl_A01_1_frame2.cget("text"))

def A01_1_Q3():
    lbl_A01_1_frame3.config(text=">>> 2*2*2*2*2\n32")
    print(lbl_A01_1_frame3.cget("text"))

def A01_1_Q4():
    lbl_A01_1_frame4.config(text=">>> print(\"5-(3-1)=\", 5-(3-1))\n5-(3-1)= 3")
    print(lbl_A01_1_frame4.cget("text"))

def A01_1_Q5():
    lbl_A01_1_frame5.config(text=">>> 10 / 2\n5.0\n>>> 10 * 2\n20")
    print(lbl_A01_1_frame5.cget("text"))

#연습문제 01_2 
def A01_2_Q1():
    lbl_A01_2_frame1.config(text=">>> print(r)\n8\n>>> x = 2 * 2 * 2\n>>> print(x)\n8\n>>> y = x / 4\
\n>>> print(y)\n2.0\n>>> z = y * y\n>>> print(z)\n4.0")
    print(lbl_A01_2_frame1.cget("text"))

#연습문제 01_3 
def A01_3_Q1():
    lbl_A01_3_frame1.config(text=">>> x = 2 * 2 * 2\n>>> print(x)\n8\n>>> x = x / 4\n>>> print(x)\n2.0\n>>> x = x * x\
\n>>> print(x)\n4.0")
    print(lbl_A01_3_frame1.cget("text"))

#연습문제 02_1 
def A02_1_Q1():
    lbl_A02_1_frame1.config(text=">>> def MH():\n\tprint(\"1+2+3+4+5=\", 1+2+3+4+5)\n\tprint(\"Simple is the best!\")\
\n\tprint(\"행복한 파이썬~\")\
\n\n>>> MH()\n1+2+3+4+5= 15\nSimple is the best!\n행복한 파이썬~\n>>> MH()\
\n1+2+3+4+5= 15\nSimple is the best!\n행복한 파이썬~\n>>>")
    print(lbl_A02_1_frame1.cget("text"))

#연습문제 02_2
def A02_2_Q1():
    lbl_A02_2_frame1.config(text=">>> def multi_string(str):\n\tprint(str)\n\tprint(str)\n\tprint(str)\
\n\n>>> multi_string(\"Hello\")\nHello\nHello\nHello")
    print(lbl_A02_2_frame1.cget("text"))

def A02_2_Q2():
    lbl_A02_2_frame2.config(text=">>> def opp_num(num):\n\tprint(num * -1)\n\n>>> opp_num(-3)\n3\
\n>>> opp_num(7)\n-7")
    print(lbl_A02_2_frame2.cget("text"))

def A02_2_Q3():
    lbl_A02_2_frame3.config(text=">>> def avr_val(n1, n2):\n\tprint((n1 + n2) / 2)\n\n>>> avr_val(3, 4)\n3.5")
    print(lbl_A02_2_frame3.cget("text"))

#연습문제 02_3
def A02_3_Q1():
    lbl_A02_3_frame1.config(text=">>> def opp_num(num):\n\treturn num * -1\n\n>>> print(opp_num(12))\n-12")
    print(lbl_A02_3_frame1.cget("text"))

def A02_3_Q2():
    lbl_A02_3_frame2.config(text=">>> def avr_val(n1, n2):\n\treturn (n1 + n2) / 2\n\n>>> print(avr_val(3, 4))\n3.5")
    print(lbl_A02_3_frame2.cget("text"))

#연습문제 03_1 
def A03_1_Q1():
    lbl_A03_1_frame1.config(text=">>> dat1 = input(\"첫 번째 입력: \")\n첫 번째 입력: 12\n>>> dat2 = input(\"두 번째 입력: \")\
\n두 번째 입력: 34\n>>> print(\"두 입력의 합:\", dat1 + dat2)\n두 입력의 합: 1234")
    print(lbl_A03_1_frame1.cget("text"))

#연습문제 03_2 
def A03_2_Q1():
    lbl_A03_2_frame1.config(text=">>> num1 = eval(input(\"첫 번째 입력: \"))\n첫 번째 입력: 1.24\n\
\n>>> num2 = eval(input(\"두 번째 입력: \"))\n두 번째 입력: 3.12\
\n>>> print(\"두 입력의 합:\", num1 + num2)\n두 입력의 합: 4.36")
    print(lbl_A03_2_frame1.cget("text"))


#연습문제 03_3
def A03_3_Q1():
    lbl_A03_3_frame1.config(text=">>> sum = 0\n>>> for i in [1, 3, 5, 7, 9]:\n\tsum = sum + i\
\n\n>>> print(sum)\n25")
    print(lbl_A03_3_frame1.cget("text"))

def A03_3_Q2():
    lbl_A03_3_frame2.config(text=">>> result = 1\n>>> for i in [2, 3, 4, 5, 6, 7, 8, 9, 10]:\n\tresult = result * i\
\n\n>>> print(result)\n3628800")
    print(lbl_A03_3_frame2.cget("text"))

def A03_3_Q3():
    lbl_A03_3_frame3.config(text=">>> for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:\n\tprint(\"7 x\", i, \"=\", 7 * i)\
\n\n7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\
\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63")
    print(lbl_A03_3_frame3.cget("text"))

def A03_3_Q4():
    lbl_A03_3_frame4.config(text=">>> for i in [9, 8, 7, 6, 5, 4, 3, 2, 1]:\n\tprint(\"7 x\", i, \"=\", 7 * i)\
\n\n7 x 9 = 63\n7 x 8 = 56\n7 x 7 = 49\n7 x 6 = 42\n7 x 5 = 35\n\
\n7 x 4 = 28\n7 x 3 = 21\n7 x 2 = 14\n7 x 1 = 7")
    print(lbl_A03_3_frame4.cget("text"))

#연습문제 03_4
def A03_4_Q1():
    lbl_A03_4_frame1.config(text=">>> for i in range(5):\n\tprint(\"안녕하세요\")\
\n\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요\n안녕하세요")
    print(lbl_A03_4_frame1.cget("text"))

def A03_4_Q2():
    lbl_A03_4_frame2.config(text=">>> for i in range(1, 10):\n\tprint(\"7 x\", i, \"=\", 7 * i)\
\n\n7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\
\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63")
    print(lbl_A03_4_frame2.cget("text"))

def A03_4_Q3():
    lbl_A03_4_frame3.config(text=">>> def exp(x, y):\n\trlt = 1\n\tfor i in range(y):\n\t\trlt = rlt * x\n\treturn rlt\n\n\
\n\n>>> exp(2, 3)\n8\n>>> exp(4, 2)\n16\n>>> exp(3, 3)\n27")
    print(lbl_A03_4_frame3.cget("text"))

def A03_4_Q4():
    lbl_A03_4_frame4.config(text=">>> def greet():\n\tnum = eval(input(\"인사를 몇 번 할까요? \"))\
\n\tfor i in range(num):\n\t\t\
print(\"반갑습니다\")\n\n>>> greet()\n인사를 몇 번 할까요? 2\n반갑습니다\n반갑습니다\
\n>>> greet()\n인사를 몇 번 할까요? 3\n반갑습니다\n반갑습니다\n반갑습니다")
    print(lbl_A03_4_frame4.cget("text"))




##타이틀 프레임(교재이미지 라벨)
title_frame = Frame(root)
title_frame.pack(padx=10, pady=10)

#교재 이미지 라벨
title_photo = PhotoImage(file="제목.PNG")
lbl_title = Label(title_frame, image=title_photo)
lbl_title.pack()


##콤보박스 프레임 (챕터 콤보박스, 챕터 버튼, 연습문제 콤보박스, 시작 버튼)
combobox_frame = Frame(root)
combobox_frame.pack(fill="x", padx=5, pady=5)

# 챕터 콤보박스
chapters = ["Chapter" + str(i) for i in range(1,4)] 
combobox_chapters = ttk.Combobox(combobox_frame, height=10, values=chapters, state="readonly")
combobox_chapters.set("CHAPTERS") 
combobox_chapters.pack(side="left", padx=3) 

#챕터 콤보박스 버튼
btn_combobox_chapters = Button(combobox_frame, text="다음", command = practices)
btn_combobox_chapters.pack(side="left", padx=3)


#연습문제 콤보박스
combobox_practices = ttk.Combobox(combobox_frame, height=10, state="readonly") 
combobox_practices.pack(side="left", padx=5)
combobox_practices.set("PRESS 다음")

#연습문제 버튼
btn_combobox_practices = Button(combobox_frame, text="문제풀이시작", command = start_solving)
btn_combobox_practices.pack(side="right", padx=5)





##문제 / 풀이 프레임(문제풀이 노트북, 정답보기 버튼)


#연습문제 01-1 노트북
Q01_1 = ttk.Notebook(root)
#Q01_1.pack(fill="both")

Q01_1_frame1 = Frame(root)
Q01_1.add(Q01_1_frame1, text="문제1")
Label(Q01_1_frame1, text="파이썬 프롬프트를 통해서 자신의 이름을 출력해보자.", justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_1_frame1, text="정답보기", command = A01_1_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A01_1_frame1 = Label(Q01_1_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_1_frame1.pack(anchor=SW, padx=5, pady=5)

Q01_1_frame2 = Frame(root)
Q01_1.add(Q01_1_frame2, text="문제2")
Label(Q01_1_frame2, text="파이썬 프롬프트를 통해서 1부터 10까지 더한 결과를 출력해보자.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_1_frame2, text="정답보기", command = A01_1_Q2).pack(anchor=W, padx=5, pady=5)
lbl_A01_1_frame2 = Label(Q01_1_frame2, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_1_frame2.pack(anchor=SW, padx=5, pady=5)

Q01_1_frame3 = Frame(root)
Q01_1.add(Q01_1_frame3, text="문제3")
Label(Q01_1_frame3, text="파이썬 프롬프트를 통해서 2를 5회 곱한 결과를 출력해보자.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_1_frame3, text="정답보기", command = A01_1_Q3).pack(anchor=W, padx=5, pady=5)
lbl_A01_1_frame3 = Label(Q01_1_frame3, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_1_frame3.pack(anchor=SW, padx=5, pady=5)

Q01_1_frame4 = Frame(root)
Q01_1.add(Q01_1_frame4, text="문제4")
Label(Q01_1_frame4, text="파이썬 프롬프트를 통해서 다음 수식의 계산 결과를 출력해보자.\
    \n5-(3-1)\n\n단, 출력의 형태는 다음과 같아야한다.\n5-(3-1) = 3", justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_1_frame4, text="정답보기", command = A01_1_Q4).pack(anchor=W, padx=5, pady=5)
lbl_A01_1_frame4 = Label(Q01_1_frame4, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_1_frame4.pack(anchor=SW, padx=5, pady=5)

Q01_1_frame5 = Frame(root)
Q01_1.add(Q01_1_frame5, text="문제5")
Label(Q01_1_frame5, text="파이썬 프롬프트를 통해서 10을 2로 나눈 결과와 10을 2로 곱한 결과를 각각 출력해보자.", \
     justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_1_frame5, text="정답보기", command = A01_1_Q5).pack(anchor=W, padx=5, pady=5)
lbl_A01_1_frame5 = Label(Q01_1_frame5, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_1_frame5.pack(anchor=SW, padx=5, pady=5)


#연습문제01-2노트북
Q01_2 = ttk.Notebook(root)
#Q01_2.pack(fill="both")

Q01_2_frame1 = Frame(root)
Q01_2.add(Q01_2_frame1, text="문제")
Label(Q01_2_frame1, text="다음 질문에 차례로 답하는 코드를 작성해보자.\
    \n질문 1. 정수2를 세 번 곱하면 얼마인가?\n질문 2. 그리고 그 결과를 4로 나누면 얼마인가?\
    \n질문 3. 끝으로 그 결과를 두 번 곱하면 얼마인가?", justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_2_frame1, text="정답보기", command = A01_2_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A01_2_frame1 = Label(Q01_2_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_2_frame1.pack(anchor=SW, padx=5, pady=5)


#연습문제01-3노트북
Q01_3 = ttk.Notebook(root)
#Q01_3.pack(fill="both")

Q01_3_frame1 = Frame(root)
Q01_3.add(Q01_3_frame1, text="문제")
Label(Q01_3_frame1, text="다음 질문에 차례로 답을 하는 코드를 작성해보자.\n단, 변수는 딱 하나만 사용해서 아래 질문에\
    답을 하도록 해야 한다.\n질문 1. 정수 2를 세번 곱하면 얼마인가?\n질문 2. 그리고 그 결과를 4로 나누면 얼마인가?\
        \n질문 3. 끝으로 그 결과를 두 번 곱하면 얼마인가?", justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q01_3_frame1, text="정답보기", command = A01_3_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A01_3_frame1 = Label(Q01_3_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A01_3_frame1.pack(anchor=SW, padx=5, pady=5)


#연습문제02-1노트북
Q02_1 = ttk.Notebook(root)
#Q02_1.pack(fill="both")

Q02_1_frame1 = Frame(root)
Q02_1.add(Q02_1_frame1, text="문제")
Label(Q02_1_frame1, text="다음 세 개의 문장을 담고 있는 함수를 정의하되 이름은 MH라 하자.\
    \n그리고 정의했다면 그 함수를 두번 이상 호출해보자.\nprint(\"1 + 2 + 3 + 4 + 5 =\", 1 + 2 + 3 + 4 + 5)\
    \nprint(\"Simple is best!\")\nprint(\"행복한 파이썬~\")", justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q02_1_frame1, text="정답보기", command = A02_1_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A02_1_frame1 = Label(Q02_1_frame1, height="300", text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A02_1_frame1.pack(anchor=SW, padx=5, pady=5)


#연습문제 02-2 노트북
Q02_2 = ttk.Notebook(root)
#Q02_2.pack(fill="both")

Q02_2_frame1 = Frame(root)
Q02_2.add(Q02_2_frame1, text="문제1")
Label(Q02_2_frame1, text="매개변수를 통해서 하나의 문자열을 전달받아서 그 전달받은 문자열을\n총 3회 출력하는 함수를 만들어보자.", \
     justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q02_2_frame1, text="정답보기", command = A02_2_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A02_2_frame1 = Label(Q02_2_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A02_2_frame1.pack(anchor=SW, padx=5, pady=5)

Q02_2_frame2 = Frame(root)
Q02_2.add(Q02_2_frame2, text="문제2")
Label(Q02_2_frame2, text="매개변수를 통해서 하나의 정수를 전달받아서 전달받은 수와 부호가 반대인 정수를 출력하는 함수를 만들어보자.\
    \n예를 들어서 함수에 3이 전달되면 -3이 출력되고 -3이 전달되면 3이 출력되어야 한다.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q02_2_frame2, text="정답보기", command = A02_2_Q2).pack(anchor=W, padx=5, pady=5)
lbl_A02_2_frame2 = Label(Q02_2_frame2, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A02_2_frame2.pack(anchor=SW, padx=5, pady=5)

Q02_2_frame3 = Frame(root)
Q02_2.add(Q02_2_frame3, text="문제3")
Label(Q02_2_frame3, text="매개변수를 통해서 두개의 정수를 전달받아서 이둘의 평균값을 계산해서 출력하는 함수를 만들어보자.\
    \n예를 들어서 이 함수에 3과 4가 전달되면 이 두 수의 평균값인 3.5가 출력되어야 한다.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q02_2_frame3, text="정답보기", command = A02_2_Q3).pack(anchor=W, padx=5, pady=5)
lbl_A02_2_frame3 = Label(Q02_2_frame3, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A02_2_frame3.pack(anchor=SW, padx=5, pady=5)


#연습문제 02-3 노트북
Q02_3 = ttk.Notebook(root)
#Q02_3.pack(fill="both")

Q02_3_frame1 = Frame(root)
Q02_3.add(Q02_3_frame1, text="문제1")
Label(Q02_3_frame1, text="하나의 정수를 전달받아서 전달받은 수와 부호가 반대인 정수를 반환하는 함수를 정의해보자.\
    \n물론 정의한 함수를 정상적으로 동작하는지 확인까지 해야 한다.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q02_3_frame1, text="정답보기", command = A02_3_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A02_3_frame1 = Label(Q02_3_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A02_3_frame1.pack(anchor=SW, padx=5, pady=5)

Q02_3_frame2 = Frame(root)
Q02_3.add(Q02_3_frame2, text="문제2")
Label(Q02_3_frame2, text="두 개의 정수를 전달받아서 그 두 수의 평균값을 계산해서 반환하는 함수를 정의해보자.",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q02_3_frame2, text="정답보기", command = A02_3_Q2).pack(anchor=W, padx=5, pady=5)
lbl_A02_3_frame2 = Label(Q02_3_frame2, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A02_3_frame2.pack(anchor=SW, padx=5, pady=5)


#연습문제 03-1 노트북
Q03_1 = ttk.Notebook(root)
#Q03_1.pack(fill="both")

Q03_1_frame1 = Frame(root)
Q03_1.add(Q03_1_frame1, text="문제1")
Label(Q03_1_frame1, text="input 함수는 프로그램 사용자가 입력한 내용을 문자열의 형태로 반환한다는 사실을 본문에서 설명하였다.\
\n따라서 이를 근거로 다음의 실행 흐름을 보이는 예를 작성해보자.\n(아래의 실행 흐름에서 12와 34는 프로그램 사용자가 입력한 값이다.)\
\n>>>____________________\n첫 번째 입력: 12\n>>>____________________\n두 번째 입력: 34\
\n>>>____________________\n두 입력의 합: 1234\
\n위의 실행 흐름에서는 프로그램 사용자가 12와 34를 입력하였다. 그리고 이 둘을 합하여 1234라는 결과를 만들어서 이를 출력하였다.\
    \n자! 그럼 이러한 실행 흐름이 진행되도록 위의 빈 공간을 채워보자.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_1_frame1, text="정답보기", command = A03_1_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A03_1_frame1 = Label(Q03_1_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_1_frame1.pack(anchor=SW, padx=5, pady=5)


#연습문제 03-2 노트북
Q03_2 = ttk.Notebook(root)
#Q03_2.pack(fill="both")

Q03_2_frame1 = Frame(root)
Q03_2.add(Q03_2_frame1, text="문제1")
Label(Q03_2_frame1, text="eval 함수와 input 함수를 잘 묶어서 사용하면 프로그램 사용자로부터 산술 연산이 가능한\
\n \‘수\’를 입력 받을 수 있음에 대해 본문에서 설명하였다. 따라서 이를 근거로 다음의 실행 흐름을 보이는 예를 작성해보자.\
\n (아래에서 1.24와 3.12는 프로그램 사용자가 입력한 값이다.)\
\n>>>____________________\n첫 번째 입력: 1.24\n>>>____________________\
\n두 번째 입력: 3.12\n>>>____________________\n두 입력의 합: 4.36\
\n위의 실행 흐름에서는 프로그램 사용자가 입력한 두 실수 1.24와 3.12를 대상으로 산술 덧셈이 진행 되었음을 보이고 있다.\
    \n 그럼 이러한 결과를 보이도록 위의 빈 공간을 채워보자.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_2_frame1, text="정답보기", command = A03_2_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A03_2_frame1 = Label(Q03_2_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_2_frame1.pack(anchor=SW, padx=5, pady=5)


#연습문제 03-3 노트북
Q03_3 = ttk.Notebook(root)
#Q03_3.pack(fill="both")

Q03_3_frame1 = Frame(root)
Q03_3.add(Q03_3_frame1, text="문제1")
Label(Q03_3_frame1, text="1, 3, 5, 7, 9의 합을 계산해서 그 결과를 출력하는 코드를 for루프를 기반으로 작성해보자.",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_3_frame1, text="정답보기", command = A03_3_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A03_3_frame1 = Label(Q03_3_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_3_frame1.pack(anchor=SW, padx=5, pady=5)

Q03_3_frame2 = Frame(root)
Q03_3.add(Q03_3_frame2, text="문제2")
Label(Q03_3_frame2, text="1부터 10까지의 곱의 결과를 계산해서 그 결과를 출력하는 코드를 for 루프를 기반으로 작성해보자.",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_3_frame2, text="정답보기", command = A03_3_Q2).pack(anchor=W, padx=5, pady=5)
lbl_A03_3_frame2 = Label(Q03_3_frame2, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_3_frame2.pack(anchor=SW, padx=5, pady=5)

Q03_3_frame3 = Frame(root)
Q03_3.add(Q03_3_frame3, text="문제3")
Label(Q03_3_frame3, text="구구단에서 7단 전부를 출력하는 코드를 for 루프를 기반으로 작성해보자.", \
     justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_3_frame3, text="정답보기", command = A03_3_Q3).pack(anchor=W, padx=5, pady=5)
lbl_A03_3_frame3 = Label(Q03_3_frame3, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_3_frame3.pack(anchor=SW, padx=5, pady=5)

Q03_3_frame4 = Frame(root)
Q03_3.add(Q03_3_frame4, text="문제4")
Label(Q03_3_frame4, text="구구단 7단을 전부 출력하되 거꾸로(7 x 9 = 63부터) 출력하는 코드를 for 루프를 기반으로 작성해보자.",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_3_frame4, text="정답보기", command = A03_3_Q4).pack(anchor=W, padx=5, pady=5)
lbl_A03_3_frame4 = Label(Q03_3_frame4, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_3_frame4.pack(anchor=SW, padx=5, pady=5)


#연습문제 03-4 노트북
Q03_4 = ttk.Notebook(root)
#Q03_4.pack(fill="both")

Q03_4_frame1 = Frame(root)
Q03_4.add(Q03_4_frame1, text="문제1")
Label(Q03_4_frame1, text="\“안녕하세요.\”를 총 5회 출력하는 코드를 for와 range 기반으로 작성해보자.",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_4_frame1, text="정답보기", command = A03_4_Q1).pack(anchor=W, padx=5, pady=5)
lbl_A03_4_frame1 = Label(Q03_4_frame1, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_4_frame1.pack(anchor=SW, padx=5, pady=5)

Q03_4_frame2 = Frame(root)
Q03_4.add(Q03_4_frame2, text="문제2")
Label(Q03_4_frame2, text="구구단 7단 전부를 출력하는 코드를 for와 range 기반으로 작성해보자.",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_4_frame2, text="정답보기", command = A03_4_Q2).pack(anchor=W, padx=5, pady=5)
lbl_A03_4_frame2 = Label(Q03_4_frame2, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_4_frame2.pack(anchor=SW, padx=5, pady=5)

Q03_4_frame3 = Frame(root)
Q03_4.add(Q03_4_frame3, text="문제3")
Label(Q03_4_frame3, text="다음 수식의 결과를 계산해서 그 값을 반환하는 함수를 for와 range 기반으로 정의해보자",\
      justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_4_frame3, text="정답보기", command = A03_4_Q3).pack(anchor=W, padx=5, pady=5)
lbl_A03_4_frame3 = Label(Q03_4_frame3, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_4_frame3.pack(anchor=SW, padx=5, pady=5)

Q03_4_frame4 = Frame(root)
Q03_4.add(Q03_4_frame4, text="문제4")
Label(Q03_4_frame4, text="\"반갑습니다.\"를 여러번 출력하는 greet이라는 이름의 함수를 만들어보자\
    \n단, 몇 번 출력할지는 프로그램 사용자에게 묻고 입력받는 형태로 작성하자.\
    \n즉 함수가 호출되면 다음과 같은 실행 흐름을 보여야한다.\n\t>>> greet()\n\t인사를 몇 번 할까요? 2\
    \n\t반갑습니다.\n\t반갑습니다.",  justify="left").pack(anchor=NW, padx=5, pady=5)
Button(Q03_4_frame4, text="정답보기", command = A03_4_Q4).pack(anchor=W, padx=5, pady=5)
lbl_A03_4_frame4 = Label(Q03_4_frame4, text="AGONY MAKE YOU STRONGER", justify="left")
lbl_A03_4_frame4.pack(anchor=SW, padx=5, pady=5)



root.mainloop()