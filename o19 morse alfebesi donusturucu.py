import winsound   # morse alfebesi kutuphamesi
uzun,kisa = 700,200    # mors uzun ve kısa kodun ne kadar olacgı tanımlandı 
menu = """Mors kodu oluşturucu/çevirici   # secme menusu
(1)Morsa çevir 
(2)Morstan çevir
(3)Çık"""                       # morse alfabesindeki harfleri tanımladık
alfabe = [["a",".-"],["b","-..."],["c","-.-."],["d","-.."],["e","."],["f","..-."],["g","--."],["h","...."],["i",".."],["j",".---"],["k","-.-"],["l",".-.."],["m","--"],["n","-."],["o","---"],["p",".--."],
          ["q","--.-"],["r",".-."],["s","..."],["t","-"],["u","..-"],["v","...-"],["w",".--"],["x","-..-"],["y","-.--"],["z","--.."],["0","-----"],["1",".----"],["2","..---"],["3","...--"],["4","....-"],["5","....."],
          ["6","-...."],["7","--..."],["8","---.."],["9","----."]]
cevirilen_metin = ""
mors = ""
morstan_cevrilen = []
def oynat():        # mors kodunu sese cevirme
    global mors     # global mors degiskeni
    for i in mors:
        if i == "-":   # karakterın uzunlugunu kontrol eder
            winsound.Beep(2000,uzun)   # uzun sesı caldırır
        if i == ".":   # karaketer kısa ise
            winsound.Beep(2000,kisa)  #kısa sesi caldrıma
while True:
    print(menu)    #  menu  ekrana yazdırma
    cevirilen_metin = ""
    morstan_cevrilen = []
    secenek = int(input("Seçiminiz:"))
    if secenek == 1:    # kullanıcıdan metın gırme 
        metin = input("Çevrilmesini istediğiniz metini giriniz:")
        for i in metin:
            for z,x in alfabe:   # alfebe ıcıne dondurme
                if i == z:   # alfebede varsa
                    cevirilen_metin += x + " "     # karsılık gelen mors kodunu yazdırma

        mors = cevirilen_metin
        print("Sonuç:",cevirilen_metin)
        oynat()    # mors sesını oynatma
    if secenek == 2:   # kullanıcı mors gırmek ıstedıgınde   
        metin = input("Çevrilmesini istediğiniz kodu giriniz:")    
        baslangic,indis = 0,0   # ındıs baslangıc degeri
        while indis < len(metin) - 1:  # morse kodunu parcalıcak dongu
            indis += 1  
            if metin[indis] == " ":   # bosluk karakterıyle karsusılasırsak 
                morstan_cevrilen.append(metin[baslangic:indis])  # morse kodunu parcala
                baslangic = indis + 1   #indıse 1 ekle 
        morstan_cevrilen.append(metin[baslangic:len(metin)])   #son parcayı da lısteye ekle
        for i in morstan_cevrilen:   # cevrılen her parca ıcn 
            for z,x in alfabe:   # alfebe ıcıne don 
                if i == x:   # alfebe ıcınde varsa
                    cevirilen_metin += z    # karsılık gelen metını ekle
                    mors += i  
        print("Sonuç:",cevirilen_metin)
        oynat()
    if secenek == 3:
        print("Yine bekleriz!")
        exit()   # programdan cık 
