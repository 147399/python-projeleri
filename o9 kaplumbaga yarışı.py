import math  # Matematiksel işlemler için gerekli olan math kütüphanesini ekliyoruz
import random  # Rastgele sayılar üretmek için gerekli olan random kütüphanesini ekliyoruz
import turtle  # Kaplumbağa grafiği çizmek için gerekli olan turtle kütüphanesini ekliyoruz
# import time  # Zaman ile ilgili işlemler için gerekli olan time kütüphanesini eklemiştik, ancak kod içinde kullanılmamış

win_length = 500  # Pencerenin uzunluğunu belirliyoruz
win_height = 500  # Pencerenin yüksekliğini belirliyoruz

turtles = 8  # Yarışacak kaplumbağa sayısını belirliyoruz

turtle.screensize(win_length, win_height)  # Turtle ekranının boyutunu ayarlıyoruz

class racer(object):  # Yarışan kaplumbağalar için bir sınıf tanımlıyoruz
    def __init__(self, color, pos):
        self.pos = pos  # Kaplumbağanın konumunu tanımlıyoruz
        self.color = color  # Kaplumbağanın rengini tanımlıyoruz
        self.turt = turtle.Turtle()  # Kaplumbağa nesnesi oluşturuyoruz
        self.turt.shape('turtle')  # Kaplumbağanın şeklini ayarlıyoruz
        self.turt.color(color)  # Kaplumbağanın rengini belirliyoruz
        self.turt.penup()  # Kalemi kaldırarak çizim yapmasını engelliyoruz
        self.turt.setpos(pos)  # Kaplumbağayı belirli bir pozisyona taşıyoruz
        self.turt.setheading(90)  # Kaplumbağanın yönünü belirliyoruz

    def move(self):  # Kaplumbağanın ilerlemesini sağlayan fonksiyon
        r = random.randrange(1, 20)  # 1 ile 20 arasında rastgele bir sayı üretiyoruz
        self.pos = (self.pos[0], self.pos[1] + r)  # Kaplumbağanın konumunu güncelliyoruz
        self.turt.pendown()  # Kalemi indirerek çizim yapmasını sağlıyoruz
        self.turt.forward(r)  # Kaplumbağayı ileri doğru hareket ettiriyoruz

    def reset(self):  # Kaplumbağanın başlangıç pozisyonuna dönmesini sağlayan fonksiyon
        self.turt.penup()  # Kalemi kaldırarak çizim yapmasını engelliyoruz
        self.turt.setpos(self.pos)  # Kaplumbağayı başlangıç pozisyonuna taşıyoruz

def setupFile(name, colors):  # Skorları saklamak için dosya oluşturan fonksiyon
    file = open(name, 'w')  # İlgili dosyayı yazma modunda açıyoruz
    for color in colors:  # Her bir renk için
        file.write(color + ' 0 \n')  # Renk ve skorunu dosyaya yazıyoruz
    file.close()  # Dosyayı kapatıyoruz

def startGame():  # Oyunu başlatan fonksiyon
    tList = []  # Kaplumbağaları tutacak bir liste oluşturuyoruz
    turtle.clearscreen()  # Turtle ekranını temizliyoruz
    turtle.hideturtle()  # Turtle'ı gizliyoruz
    colors = ["red", "green", "blue", 'yellow', 'pink', 'orange', 'purple', 'black', 'grey']  # Kaplumbağaların renkleri
    start = -(win_length/2) + 20  # Başlangıç pozisyonunu belirliyoruz
    for t in range(turtles):  # Kaplumbağa sayısı kadar döngü
        newPosX = start + t*(win_length)//turtles  # Yeni pozisyonu hesaplıyoruz
        tList.append(racer(colors[t],(newPosX, -230)))  # Yeni bir kaplumbağa oluşturup listeye ekliyoruz
        tList[t].turt.showturtle()  # Kaplumbağayı gösteriyoruz

    run = True  # Oyunun devam edip etmediğini kontrol eden değişken
    while run:  # Oyun devam ettiği sürece
        for t in tList:  # Her bir kaplumbağa için
            t.move()  # Hareket etmelerini sağlıyoruz

        maxColor = []  # En çok ilerleyen kaplumbağaların renklerini tutacak liste
        maxDis = 0  # En büyük ilerleme değeri
        for t in tList:  # Her bir kaplumbağa için
            if t.pos[1] > 230 and t.pos[1] > maxDis:  # Eğer kaplumbağa bitiş çizgisini geçtiyse ve en büyük ilerleme değerini geçmişse
                maxDis = t.pos[1]  # Yeni en büyük ilerleme değerini güncelliyoruz
                maxColor = []  # En çok ilerleyen kaplumbağaların renklerini temizliyoruz
                maxColor.append(t.color)  # Bu kaplumbağanın rengini listeye ekliyoruz
            elif t.pos[1] > 230 and t.pos[1] == maxDis:  # Eğer kaplumbağa bitiş çizgisini geçtiyse ve en büyük ilerleme değerine eşitse
                maxDis = t.pos[1]  # En büyük ilerleme değerini güncelliyoruz
                maxColor.append(t.color)  # Bu kaplumbağanın rengini listeye ekliyoruz

        if len(maxColor) > 0:  # Eğer en az bir kaplumbağa bitiş çizgisini geçmişse
            run = False  # Oyunu durduruyoruz
