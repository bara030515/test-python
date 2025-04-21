import tkinter
import tkinter.messagebox as msgbox
import random

#좌표 출력기
def mouseMove(event):
    x = event.x
    y = event.y    
    labelMouse["text"]=str(x)+","+str(y)

def click_btnCheck():
    global count, btnCheck
    #입력 유효성 확인
    if (entryLec1.get() == "") or (entryLec2.get() == "") or (entryLec3.get() == "") :
        return
    elif (len(entryLec1.get()) != 1) or (len(entryLec2.get()) != 1) or (len(entryLec3.get()) != 1):
        return
    
    btnCheck["state"] = "disabled"              #추가 입력 금지
    count += 1                                  #시도 횟수 증가
    successGame = False                         #성공 여부 확인 변수
    #-------------------과제 영역 시작-----------------------#
    #정답인 경우 successGame를 참으로 지정

    # 스트라이크와 볼의 초기값
    strike = 0
    ball = 0

    # if 사용자가 입력한 첫 번째 숫자가 임의의 숫자 첫 번째와 맞으면 스트라이크 +1
    # elif 사용자가 입력한 첫 번째 숫자가 임의의 숫자 두 번째 혹은 세 번째와 맞으면 볼 +1
    if answer[0] == entryLec1.get():
        strike += 1
    elif (answer[0] == entryLec2.get()) or (answer[0] == entryLec3.get()):
        ball += 1

    # if 사용자가 입력한 두 번째 숫자가 임의의 숫자 두 번째와 맞으면 스트라이크 +1
    # elif 사용자가 입력한 두 번째 숫자가 임의의 숫자 첫 번째 혹은 세 번째와 맞으면 볼 +1
    if answer[1] == entryLec2.get():
        strike += 1
    elif (answer[1] == entryLec1.get()) or (answer[1] == entryLec3.get()):
        ball += 1

    # if 사용자가 입력한 첫 번째 숫자가 임의의 숫자 첫 번째와 맞으면 스트라이크 +1
    # elif 사용자가 입력한 첫 번째 숫자가 임의의 숫자 두 번째 혹은 세 번째와 맞으면 볼 +1
    if answer[2] == entryLec3.get():
        strike += 1
    elif (answer[2] == entryLec1.get()) or (answer[2] == entryLec2.get()):
        ball += 1
    
    # 3스트라이크가 되면 succesGame을 트루로 바꿔라 (과제 영역 아래 쪽에 트루면 성공 문구와 함께 프로그램 종료하는 코드 있음)
    if strike == 3:
        successGame = True

    # 버튼에 스트라이크와 볼의 개수를 보여주는 코드
    output_str = str(strike)+"S"+" "+str(ball)+"B"
    btnCheck["text"] = (output_str)

    # print (strike, ball) 함수 테스트

    #------------------- 과제 영역 끝 -----------------------#

    # Game End (9번의 기회를 모두 사용한 경우)
    if count == 10 :
        response = msgbox.showerror("종료","아쉽게도 모든 기회를 사용했습니다. \n 정답은"+answer+"입니다")
        if response:
            root.destroy()
    
    elif successGame == True:
        response = msgbox.showinfo("성공","정답입니다. \n 정답은"+answer+"입니다")
        if response:
            root.destroy()

    else:
        nextGame()

def nextGame():
    global entryLec1, entryLec2, entryLec3, btnCheck
    labelCount = tkinter.Label(root, text=str(count)+"회", font=("맑은 고딕",10))
    labelCount.place(x=15,y=15+count*25)

    entryLec1 = tkinter.Entry(width=2)
    entryLec2 = tkinter.Entry(width=2)
    entryLec3 = tkinter.Entry(width=2)

    entryLec1.place(x=60,y=15+count*25)
    entryLec2.place(x=90,y=15+count*25)
    entryLec3.place(x=120,y=15+count*25)

    btnCheck = tkinter.Button(root, text="확인", font=("Times New Roma",10),command=click_btnCheck)
    btnCheck.place(x=150, y=15+count*25,width=70,height=20)

root = tkinter.Tk()
root.title("야구 게임")
root.geometry("250x270")

#좌표 출력기
root.bind("<Motion>", mouseMove)
labelMouse = tkinter.Label(root, text=",", font=("맑은 고딕",10))
labelMouse.place(x=0,y=250)

#문제 횟수 초기값
count = 1

#문제 제출
answer = str(random.randint(100,999))
print(answer)
while (answer[0] == answer[1]) or (answer[1] == answer[2]) or (answer[0] == answer[2]):
    answer = str(random.randint(100,999))
    print(answer)

nextGame()

root.mainloop()

#tkinter문제 2개, 이론 짧음 거의 실습 문제
#결과 + 의도를 주면 코드를 작성
