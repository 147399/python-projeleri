import turtle
from turtle import*

# Turtle'ı gizle
hideturtle()

# Ekran oluştur
wn = Screen()
wn.bgcolor('black')

# Yeni bir Turtle nesnesi oluştur
t = turtle.Turtle()
t.pencolor('white')  # Kalem rengini beyaz yap

# Eğri çizmek için fonksiyon tanımla
def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

# Kalp şeklini çizmek için fonksiyon tanımla
def heart():
    t.fillcolor('red')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

# Kalp şeklini çiz
heart()

# Turtle'ı gizle
t.ht()

# Mesaj yazmak için fonksiyon tanımla
def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.color('white')
    style = ('Stencil Std', 18, 'italic')  # Yazı stili
    t.write(message, font=style)  # Mesajı yaz

# İsteğe bağlı mesajları yaz
write('I', (-68, 95))
write('L', (-55, 95))
write('O', (-42, 95))
write('V', (-27, 95))
write('E', (-13, 95))
write('Y', (10, 95))
write('O', (26, 95))
write('U', (45, 95))

# Ekranı kapatmak için mainloop'u çağır
wn.mainloop()