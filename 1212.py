import time
from tkinter import * 

window = Tk()

canvas1 = Canvas(window,bg = "white",width=300,height=200)
canvas1.pack()

id = canvas1.create_text(100,100,text="파이썬 커피샵으로 오세요")

while True:
    canvas1.move(id,-2,0)
    window.update()
    time.sleep(0.05)

    for i in canvas1:
        canvas1.move(id,2,0)
        window.update()
        time.sleep(0.05)

        


