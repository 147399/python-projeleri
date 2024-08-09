# FizzBuzz problemini çözmek için üç farklı yöntem

# İlk yöntem: Basit if-elif yapısı
for i in range(1, 101):  # 1'den 100'e kadar sayıları iterasyonla döner
    if i % 15 == 0:  # Hem 3'e hem 5'e bölünüyorsa
        print("fizzbuzz")
    elif i % 3 == 0:  # Sadece 3'e bölünüyorsa
        print("fizz")
    elif i % 5 == 0:  # Sadece 5'e bölünüyorsa
        print("buzz")
    else:  # Hiçbirine bölünmüyorsa
        print(i)


# İkinci yöntem: Dinamik bir çıktı oluşturma
for i in range(1, 101):  # 1'den 100'e kadar sayıları iterasyonla döner
    cıktı = ""  # Boş bir string ile başlar
    if i % 3 == 0:  # 3'e bölünüyorsa
        cıktı += "fizz"
    if i % 5 == 0:  # 5'e bölünüyorsa
        cıktı += "buzz"
    if i % 7 == 0:  # 7'ye bölünüyorsa
        cıktı += "guzz"
    if cıktı == "":  # Hiçbirine bölünmüyorsa
        cıktı += str(i)  
    print(cıktı)


# Üçüncü yöntem: Sözlük kullanarak dinamik çıktı oluşturma
cıktılar = {3: "fizz", 5: "buzz", 7: "guzz"}  # Bölme koşulları ve karşılık gelen kelimeler
for i in range(1, 101):  # 1'den 100'e kadar sayıları iterasyonla döner
    cıktı = ""  # Boş bir string ile başlar
    for kosul in cıktılar.keys():  # Sözlükteki her koşul için döner
        if i % kosul == 0:  # Sayı koşula bölünüyorsa
            cıktı += cıktılar[kosul]  # Karşılık gelen kelimeyi ekler
    if cıktı == "":  # Hiçbirine bölünmüyorsa
        cıktı = str(i)
    print(cıktı)