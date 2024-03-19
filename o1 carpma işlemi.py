from random import randint  # randint fonksiyonunu içe aktarır

"""
    Küçük çapta bir çarpım tablosu uygulaması
"""

print("-" * 50)  # 50 tane tire yazdırır
print("\t\tHOŞGELDİNİZ..")  # HOŞGELDİNİZ.. yazısını ekrana yazdırır
print("-" * 50, "\n")  # 50 tane tire yazdırır ve bir alt satıra geçer

def carpim(i, j, r):
    """
    İki sayının çarpımını hesaplar ve sonucu kontrol eder.
    :param i: Birinci sayı
    :param j: İkinci sayı
    :param r: Kullanıcının girdiği cevap
    """
    if r != "-1":
        result = str(i * j)  # i ve j sayılarını çarpar
        if result == r:  # Çıkan sonuc, kullanıcının girdiği cevapla karşılaştırılır
            print("\t\t***** Doğru *****")
        else:
            print("\t!!! Yanlış cevap %s olacaktı" % result)  # Yanlış cevap durumunda doğru cevabı gösterir
    else:
        secim()  # r -1 ise başka bir seçeneğe geçilir


def basla(rng_1, rng_2):
    """
    Belirli bir aralıkta rastgele çarpım soruları üretir ve kullanıcıdan cevap alır.
    :param rng_1: Soruların rastgele üretilmesi için minimum sayı
    :param rng_2: Soruların rastgele üretilmesi için maksimum sayı
    """
    if rng_1 > 10:
        x = 10
    else:
        x = 5
    for i in range(0, x):
        for j in range(0, x):
            sayi_1 = randint(rng_1, rng_2)  # rng_1 ve rng_2 arasında rastgele bir sayı oluşturur
            sayi_2 = randint(rng_1, rng_2)  # rng_1 ve rng_2 arasında rastgele bir sayı oluşturur
            print("_" * 50, "\n")  # 50 tane alt çizgi yazdırır ve bir alt satıra geçer
            print("\t%d x %d kaça eşittir? (çıkış = 000)" % (sayi_1, sayi_2))  # Çarpım sorusunu yazdırır
            sonuc = input("sonuc >> ")  # Kullanıcıdan cevap alır
            carpim(sayi_1, sayi_2, sonuc)  # Kullanıcının cevabını kontrol eder

            if i == 4 and j == 4:  # İki döngü de 5'e ulaştığında bir üst bölüme geçiş sağlar
                print("\n *-- Bu bölüm bitti bir üst bölüme geçebilsiniz --*\n")
                secim()  # Bir üst bölüme geçiş yapar


def secim():
    """
    Kullanıcıya seviye seçimi yapma imkanı verir.
    """
    print(" Hangi seviyeden başlamak istiyorsunuz (çıkış = 000) ?\n")
    print("  1 - Kolay ")
    print("  2 - Orta ")
    print("  3 - Zor")
    print("  4 - Çok zor\n")

    svy = input(" >> ")  # Kullanıcıdan seviye seçimi alır

    if svy == "1":
        basla(1, 10)  # Kolay seviyede başlatır

    elif svy == "2":
        basla(5, 12)  # Orta seviyede başlatır

    elif svy == "3":
        basla(10, 25)  # Zor seviyede başlatır

    elif svy == "4":
        basla(10, 100)  # Çok zor seviyede başlatır

    else:
        exit(0)  # Programı sonlandırır


if __name__ == '__main__':
    secim()  # Programı başlatır ve seviye seçimi için kullanıcıya yönlendirir
