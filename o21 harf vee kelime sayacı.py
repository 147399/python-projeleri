
"""
def kelime_say(text):


    kelimeler = text.split()

    return len(kelimeler)



metin= input("lutfen metını girin : ")


kelimesayisi = kelime_say(metin)

print(f"metindeki kelime sayısı :{kelimesayisi} ")


"""




def kelime_say(text):
    """
    Verilen metindeki kelime sayısını döndüren fonksiyon.

    Args:
        text (str): Kelime sayısının hesaplanacağı metin.

    Returns:
        int: Metindeki kelime sayısı.
    """
    # Metni boşluk karakterlerinden bölerek bir liste oluşturuyoruz
    kelimeler = text.split()

    # Kelime sayısını döndürüyoruz
    return len(kelimeler)


# Kullanıcıdan metin girmesini istiyoruz
metin = input("Lütfen metni girin: ")

# Kelime sayma fonksiyonunu çağırarak metindeki kelime sayısını alıyoruz
kelime_sayisi = kelime_say(metin)

# Sonucu ekrana yazdırıyoruz
print(f"Metindeki kelime sayısı: {kelime_sayisi}")  







def harf_say(text):
    """
    Verilen metindeki harf sayısını döndüren fonksiyon.

    Args:
        text (str): Harf sayısının hesaplanacağı metin.
dsv
    Returns:
        int: Metindeki harf sayısı.
    """
    # Metindeki boşluk, noktalama işareti ve rakam karakterlerini temizliyoruz
    temiz_metin = ''.join(c for c in text if c.isalpha())

    # Temizlenmiş metnin uzunluğunu döndürüyoruz (bu, harf sayısını temsil eder)
    return len(temiz_metin)


# Kullanıcıdan metin girmesini istiyoruz
metin = input("Lütfen metni girin: ")

# Harf sayma fonksiyonunu çağırarak metindeki harf sayısını alıyoruz
harf_sayisi = harf_say(metin)

# Sonucu ekrana yazdırıyoruz
print(f"Metindeki harf sayısı: {harf_sayisi}")





