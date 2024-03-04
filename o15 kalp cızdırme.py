import math  # Matematik işlemleri için math kütüphanesini içeri aktar
hideturtle()     # fareyı gızler

from turtle import  *  # Turtle grafiği oluşturmak için turtle kütüphanesini içeri aktar

# Kalp şeklini oluşturmak için gerekli matematiksel fonksiyonlar
def hearta(k):
    return 15 * math.sin(k) ** 3

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)  # Turtle'ın çizim hızını ayarla (0: en hızlı, 1: yavaş, 10: en yavaş)

bgcolor("black")  # Arka plan rengini siyah yap

for i in range(90000):
    # Kalp şeklini oluşturmak için belirli noktalara git
    goto(hearta(i) * 20, heartb(i) * 20)

    # Kalp rengini kırmızı yap
    color("red")

    # Orjine geri dön
    goto(0, 0)

done()  # Turtle grafiğini tamamlar ve kapatır