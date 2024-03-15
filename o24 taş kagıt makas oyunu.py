import random

def oyunu_oyna():
    # Taş, kağıt, makas seçeneklerini içeren bir liste oluşturuluyor
    liste = ["taş", "kağıt", "makas"]
    # Oyuncunun ve bilgisayarın skorları başlangıçta sıfır olarak ayarlanıyor
    oyuncu_skor = 0
    pc_skor = 0
    # Toplam oyun sayısı ve kazanma limiti belirleniyor
    toplam_oyun = 0
    kazanma_limiti = 3

    # Oyuncu veya bilgisayarın skoru kazanma limitine ulaşana kadar oyun devam ediyor
    while True:
        # Kazanma limitine ulaşıldığında döngüden çıkılıyor
        if oyuncu_skor == kazanma_limiti or pc_skor == kazanma_limiti:
            break

        # Bilgisayar rastgele bir seçim yapıyor
        pc = random.choice(liste)
        # Oyuncudan seçim yapması isteniyor
        player = input("Taş mı, kağıt mı, makas mı? (Çıkmak için 'E' tuşuna basın): ")

        # Oyuncu 'E' tuşuna basarak çıkmak istiyorsa döngüden çıkılıyor
        if player.lower() == 'e':
            break

        # Oyuncunun seçimi geçerli mi kontrol ediliyor
        if player.lower() not in liste:
            print("Geçersiz bir seçim yaptınız.")
            continue

        # Bilgisayarın ve oyuncunun seçimleri ekrana yazdırılıyor
        print("PC", pc, "seçti")
        print("Player", player, "seçti")

        # Oyunun sonucuna göre skorlar güncelleniyor
        if player.lower() == pc:
            print("Berabere!")
        elif (player.lower() == "taş" and pc == "makas") or \
                (player.lower() == "kağıt" and pc == "taş") or \
                (player.lower() == "makas" and pc == "kağıt"):
            print("Kazandınız!")
            oyuncu_skor += 1
        else:
            print("Kaybettiniz!")
            pc_skor += 1

        # Toplam oynanan oyun sayısı bir arttırılıyor
        toplam_oyun += 1

    # Oyun bittiğinde sonuçlar ekrana yazdırılıyor
    print("Oyun bitti!")
    print("Toplam oynanan oyun sayısı:", toplam_oyun)
    print("Oyuncu skoru:", oyuncu_skor)
    print("PC skoru:", pc_skor)

if __name__ == "__main__":
    oyunu_oyna()

































