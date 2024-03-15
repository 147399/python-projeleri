def topla(x, y):
    return x + y  # İki sayıyı toplar ve sonucu döndürür

def cikar(x, y):
    return x - y  # İki sayıyı çıkarır ve sonucu döndürür

def carp(x, y):
    return x * y  # İki sayıyı çarpar ve sonucu döndürür

def bol(x, y):
    if y == 0:
        return "Sıfıra bölme hatası!"  # Eğer bölünen sıfırsa hata mesajı döndürür
    else:
        return x / y  # İki sayıyı böler ve sonucu döndürür

print("Yapmak istediğiniz işlemi seçin:")  # Kullanıcıya işlem seçimini belirtir
print("1. Toplama")  # Toplama işlemini kullanıcıya belirtir
print("2. Çıkarma")  # Çıkarma işlemini kullanıcıya belirtir
print("3. Çarpma")  # Çarpma işlemini kullanıcıya belirtir
print("4. Bölme")  # Bölme işlemini kullanıcıya belirtir

secim = input("Seçiminizi yapın (1/2/3/4): ")  # Kullanıcıdan işlem seçimini alır

num1 = float(input("Birinci sayıyı girin: "))  # Kullanıcıdan birinci sayıyı alır
num2 = float(input("İkinci sayıyı girin: "))  # Kullanıcıdan ikinci sayıyı alır

if secim == '1':
    print(num1, "+", num2, "=", topla(num1, num2))  # Toplama işlemini gerçekleştirir ve sonucu ekrana yazdırır

elif secim == '2':
    print(num1, "-", num2, "=", cikar(num1, num2))  # Çıkarma işlemini gerçekleştirir ve sonucu ekrana yazdırır

elif secim == '3':
    print(num1, "*", num2, "=", carp(num1, num2))  # Çarpma işlemini gerçekleştirir ve sonucu ekrana yazdırır

elif secim == '4':
    print(num1, "/", num2, "=", bol(num1, num2))  # Bölme işlemini gerçekleştirir ve sonucu ekrana yazdırır

else:
    print("Geçersiz giriş")  # Geçersiz bir seçim yapıldığında kullanıcıya bilgi verir




