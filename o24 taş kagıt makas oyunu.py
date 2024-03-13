import random

def oyunu_oyna():
    liste = ["taş", "kağıt", "makas"]
    oyuncu_skor = 0
    pc_skor = 0
    toplam_oyun = 0
    kazanma_limiti = 3

    while True:
        if oyuncu_skor == kazanma_limiti or pc_skor == kazanma_limiti:
            break

        pc = random.choice(liste)
        player = input("Taş mı, kağıt mı, makas mı? (Çıkmak için 'E' tuşuna basın): ")

        if player.lower() == 'e':
            break

        if player.lower() not in liste:
            print("Geçersiz bir seçim yaptınız.")
            continue

        print("PC", pc, "seçti")
        print("Player", player, "seçti")

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

        toplam_oyun += 1

    print("Oyun bitti!")
    print("Toplam oynanan oyun sayısı:", toplam_oyun)
    print("Oyuncu skoru:", oyuncu_skor)
    print("PC skoru:", pc_skor)

if __name__ == "__main__":
    oyunu_oyna()

    




























