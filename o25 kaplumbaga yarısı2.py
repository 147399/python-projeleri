import turtle
import time

class Yaris:
    def __init__(self):
        # Turtle ekranını oluştur
        self.win = turtle.Screen()
        # Ekran boyutunu ayarla
        self.win.setup(width=700, height=700)
        # Ekran rengini beyaz yap
        self.win.bgcolor("white")

        # Kırmızı yarışmacıyı oluştur
        self.kirmizi = turtle.Turtle()
        # Yarışmacı rengini kırmızı yap
        self.kirmizi.color("red")
        # Yarışmacı şeklini ok şekline getir
        self.kirmizi.shape("arrow")
        # Yarışmacıyı kaldır
        self.kirmizi.penup()
        # Yarışmacıyı belirli bir konuma taşı
        self.kirmizi.goto(-200, -280)
        # Yarışmacıyı yukarı bakacak şekilde döndür
        self.kirmizi.setheading(90)

        # Mavi yarışmacıyı oluştur
        self.mavi = turtle.Turtle()
        # Yarışmacı rengini mavi yap
        self.mavi.color("blue")
        # Yarışmacı şeklini kaplumbağa şekline getir
        self.mavi.shape("turtle")
        # Yarışmacıyı kaldır
        self.mavi.penup()
        # Yarışmacıyı belirli bir konuma taşı
        self.mavi.goto(200, -280)
        # Yarışmacıyı yukarı bakacak şekilde döndür
        self.mavi.setheading(90)

        # Kırmızı yarışmacının skorunu tut
        self.skor_kirmizi = 0
        # Mavi yarışmacının skorunu tut
        self.skor_mavi = 0

        # Klavye olaylarını dinle
        self.win.listen()
        # Mavi yarışmacıyı yukarı taşı
        self.win.onkeypress(self.mavi_yukari, "Up")
        # Kırmızı yarışmacıyı yukarı taşı
        self.win.onkeypress(self.kirmizi_yukari, "w")

        # Çizgiyi çiz
        pen = turtle.Turtle()
        pen.penup()
        pen.goto(-350, 350)
        pen.pendown()
        pen.forward(700)
        pen.hideturtle()

        # Çizginin y koordinatını sakla
        self.line_y = pen.ycor()

    def mavi_yukari(self):
        # Mavi yarışmacıyı yukarı taşı
        self.mavi.sety(self.mavi.ycor() + 20)
        # Eğer mavi yarışmacı çizgiyi geçerse, yarışı sıfırla
        if self.mavi.ycor() >= self.line_y:
            self.yarisi_sifirla()

    def kirmizi_yukari(self):
        # Kırmızı yarışmacıyı yukarı taşı
        self.kirmizi.sety(self.kirmizi.ycor() + 20)
        # Eğer kırmızı yarışmacı çizgiyi geçerse, yarışı sıfırla
        if self.kirmizi.ycor() >= self.line_y:
            self.yarisi_sifirla()

    def yarisi_sifirla(self):
        # Yarışı sıfırla
        self.skor_kirmizi = 0
        self.skor_mavi = 0
        self.mavi.goto(200, -280)
        self.kirmizi.goto(-200, -280)

    def basla(self):
        # Yarışmayı başlat
        self.win.mainloop()

# Yarış sınıfını oluştur ve başlat
yaris = Yaris()
yaris.basla()