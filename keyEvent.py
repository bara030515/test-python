import tkinter

# 전역 변수
key = 0
cx = 400
cy = 300

# 함수 영역
def main_proc():
    global cx, cy, key
    # label["text"] = key
    if key == 'Up':
        cy = cy -20
    if key == 'Down':
        cy = cy +20
    if key == 'Left':
        cx = cx -20
    if key == 'Right':
        cx = cx +20

    # 시간에 따라 캐릭터가 내려감
    cy += 10
    # 변경된 유치의 경계를 확인
    if cy < 70 : cy = 70
    if cy > 600-70 : cy = 600-70
    if cx < 70 : cx = 70
    if cx > 800-70 : cx = 800-70

    canvas.coords("춘식", cx, cy)
    root.after(100, main_proc)

def key_down(e):
    global key
    key = e.keysym

def key_up(e):
    global key
    key = 0


# 메인 영역
root = tkinter.Tk()
root.title("키 이벤트")
root.bind("<KeyPress>", key_down)
root.bind("<KeyRelease>", key_up)
# label = tkinter.Label(font=("맑은 고딕", 80))
# label.pack()
canvas = tkinter.Canvas(width=800, height= 600, bg= '#FFB6C1')
canvas.pack()

img = tkinter.PhotoImage(file="춘식.png")
canvas.create_image(400, 300, image= img, tag = "춘식")


main_proc()
root.mainloop()