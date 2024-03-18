import turtle
from random import randint

t = turtle.Turtle()


maxy = 500
maxx= 500

t.reset
t.speed(0)
turtle.colormode(255)

for i in range(1000):
    ycap= randint(10,100)
    y = randint(-maxy,maxy)
    x = randint(-maxx,maxx)
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    renk = (r,g,b)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color((0,0,0), renk)
    t.begin_fill()
    t.circle(ycap)
    t.end_fill()

t.hideturtle()
turtle.mainloop()
