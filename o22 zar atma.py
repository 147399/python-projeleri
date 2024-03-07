

import random 
import os
import time

# Başlık
print("Zar Atma Simülasyonu")
print("." * 50)

# Sonsuz döngü başlatılır
while True:
    # Kullanıcıya zar atma işlemini onaylaması istenir
    zarat = input("Zar atmayı onaylıyor musunuz: ")
    print("Zar atılıyor...")
    time.sleep(2)  # 2 saniye beklenir
    print("." * 50)
    
    # Rastgele bir zar değeri seçilir ve ekrana yazdırılır
    print("Zar = {} geldi".format(random.randint(1, 6)))
    print("." * 50)
    
    # Kullanıcıya tekrar zar atmak isteyip istemediği sorulur
    soru = input("Zarı tekrar atmak ister misiniz? (Evet için 'E', Hayır için 'H' yazınız): ")
    
    # Kullanıcının cevabına göre işlem yapılır
    if soru.upper() == "E":  # Eğer cevap 'E' ise
        #if os.name == 'nt':  # Eğer işletim sistemi Windows ise
          # os.system('cls')  # Ekran temizlenir
        print("Zarı tekrar deneyebilirsiniz")
        print("." * 50)
    else:  # Eğer cevap 'E' değilse
        print("Programdan çıktınız")
        break  # Döngü sonlandırılır