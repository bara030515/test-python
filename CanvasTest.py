import tkinter
import tkinter.font
import random
root = tkinter.Tk()
root.title("캔버스 만들기")

#캔버스 만들기
canvas = tkinter.Canvas(root, width=800, height=600, bg = "#FFFFFF")
canvas.pack()

#버튼 클릭하면 제비뽑기 실행
def click_btnLot():
    labelRandom['text'] = random.choice(['대길', '중길', '소길', '흉'])
    text.insert(tkinter.END, labelRandom['text']+"\n")

#마우스 좌표 함수
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse.config(text=str(x)+','+str(y))
    labelMouse.place(x=0,y=200)

#캔버스에 이미지 넣기
bgtimg = tkinter.PhotoImage(file="miko.png")
canvas.create_image(400,300,image=bgtimg)

canvas.create_rectangle(351,394,620,540, fill='darkgray', outline='red', width='5')

#마우스 좌표 라벨

root.bind('<Motion>',mouseMove)
labelMouse = tkinter.Label(root, text=',', font=("맑은 고딕", 10))
labelMouse.pack()


#제비뽑기 결과 라벨
labelRandom = tkinter.Label(root, text='??', font=('맑은 고딕', 100), bg = "#FFFFFF")
labelRandom.place(x=384, y=67)

#제비뽑기 실행 버튼
btnLot = tkinter.Button(root, text='제비뽑기', font=('맑은 고딕', 40), fg = "skyblue", command=click_btnLot)
btnLot.place(x=360, y=403)


text = tkinter.Text()
text.place(x=20, y=0, width=800, height=400)

root.mainloop()