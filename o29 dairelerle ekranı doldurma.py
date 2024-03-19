import turtle  # turtle modülünü içe aktarır
from random import randint  # randint fonksiyonunu içe aktarır

t = turtle.Turtle()  # turtle için bir nesne oluşturur

maxy = 500  # maksimum y koordinatı
maxx = 500  # maksimum x koordinatı

t.reset()  # turtle'ı sıfırlar
t.speed(0)  # turtle'ın çizim hızını ayarlar
turtle.colormode(255)  # renk modunu RGB değerleriyle ayarlar

for i in range(1000):  # 1000 kere döngüye girer
    ycap = randint(10, 100)  # yarıçapı rastgele belirler
    y = randint(-maxy, maxy)  # y koordinatını rastgele belirler
    x = randint(-maxx, maxx)  # x koordinatını rastgele belirler
    r = randint(0, 255)  # kırmızı bileşeni rastgele belirler
    g = randint(0, 255)  # yeşil bileşeni rastgele belirler
    b = randint(0, 255)  # mavi bileşeni rastgele belirler
    renk = (r, g, b)  # rastgele renk oluşturur
    t.penup()  # kalem kaldırır
    t.goto(x, y)  # belirlenen koordinatlara gider
    t.pendown()  # kalem iner
    t.color((0, 0, 0), renk)  # çizgi ve dolgu rengini belirler
    t.begin_fill()  # dolgu alanı çizimini başlatır
    t.circle(ycap)  # belirlenen yarıçapta bir daire çizer
    t.end_fill()  # dolgu alanı çizimini sonlandırır

t.hideturtle()  # turtle'ı gizler
turtle.mainloop()  # ana döngüyü başlatır ve pencereyi açık tutar
