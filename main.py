import tkinter as tk
import winsound

# 타이머 그리기
import winsound


def draw() :
    global sec
    global color

    timer.delete("all")
    timer.create_arc(30, 30, 200, 200,
                     fill=color, outline=color, width=0,
                     start=90, extent=sec)



# 카운트다운
def countDown() :
    global sec
    global pause

    if pause is False :
        draw()
        sec -= 0.1
        if(sec < 0) :
            btnReset()
            winsound.PlaySound('alarm.wav', winsound.SND_FILENAME)
        window.after(1000, countDown)



# 시작 버튼
def btnStart() :
    global color
    global pause

    color = 'red'
    pause = False

    countDown()



# 일시정지 버튼
def btnPause() :
    global color
    global pause

    color = 'green'
    pause = True

    draw()



# 리셋 버튼
def btnReset() :
    global sec
    global color
    global pause

    color = 'blue'
    pause = True
    sec = 359.9

    draw()



# 메인
if __name__ == "__main__" :
    window = tk.Tk()
    window.title("time for pie")
    window.geometry("250x300")
    window.resizable(False, False)
    window.configure(bg='white')
    window.iconbitmap('./icon.ico')

    # 원형 타이머
    timer = tk.Canvas(window, width=230, height=230, bg='white', highlightthickness=0)
    timer.pack(side='top')
    btnReset()

    # 시작 버튼
    startButton = tk.Button(window, text="start", command=lambda:btnStart())
    startButton.pack(side='left')

    # 일시정지 버튼
    pauseButton = tk.Button(window, text="pause", command=lambda:btnPause())
    pauseButton.pack(side='left')

    # 리셋 버튼
    resetButton = tk.Button(window, text="reset", command=lambda:btnReset())
    resetButton.pack(side='right')

    window.mainloop()
