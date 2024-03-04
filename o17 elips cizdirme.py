from turtle import speed, bgcolor, colormode, fd, rt, pencolor, hideturtle

# Fareyi gizle
hideturtle()

# Çizim hızını ayarla
speed(15)

# Arka plan rengini siyah yap
bgcolor("black")

# Renk modunu ayarla
colormode(255)

# Başlangıç renk değerleri
r, g, b = 255, 0, 0

# Renk geçişleri için döngü
for i in range(255 * 2):
    # Renk geçişlerini kontrol et ve renk değerlerini güncelle
    if i < 255 // 3:
        g += 3
    elif i < (255 * 2) // 3:
        r -= 3
    elif i < 255:
        b += 3
    elif i < (255 * 4) // 3:
        g -= 3
    elif i < (255 * 5) // 3:
        r += 3
    else:
        b -= 3
    
    # İleri git ve dön
    fd(50 + i)
    rt(91)
    
    # Kalem rengini güncelle
    pencolor(r, g, b)
    
