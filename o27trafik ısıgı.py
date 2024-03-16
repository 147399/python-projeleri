from turtle import * 
import time

w = Screen()
w.setup(400,700)
w.title 


penup()
goto(0,180)
pendown()
pensize(4)



for i in range(2):
    forward(80)
    right(90)
    forward(220)
    right(90)

def kirmizi():
    penup()
    goto(40,140)
    fillcolor('red')
    shape('circle')
    shapesize(3)

def sari():
    penup()
    goto(40,70)
    fillcolor('yellow')
    shape('circle')
    shapesize(3)

def yeşil():
    penup()
    goto(40,0)
    fillcolor('green')
    shape('circle')
    shapesize(3)


while True :
    yeşil()
    time.sleep(3)
    sari()
    time.sleep(3)
    kirmizi()
    time.sleep(3)
    sari()
    time.sleep(3)



w.mainloop()