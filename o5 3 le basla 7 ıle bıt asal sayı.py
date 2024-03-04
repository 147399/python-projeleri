

prime_list = list()

prime_list.append(2)


sayi = 3 

while True : 
    prime = True                # dongu dogru oldugu surece dondur 
    for i in range(2,int(sayi ** 0.5) +1 ):       # 2 den basla sayıya kadar git
        if sayi %i == 0:          # sayı bolu i = 0 sa sayı asal degıl 
            prime = False
            break 
                               
    if prime:
        prime_list.append(sayi)         # sayıları listeler 
        if len(prime_list)    == 100:  # 100 e kadar olan degerleri alır      
          break 


    sayi  += 1 
                                                                                                                                                                
liste2 = []                                                              # yeni lıste adı 
for prime in prime_list :                  
    strprime = str(prime)                                                  # prime listesini  strınge cevirir 
    if strprime.startswith("3") and strprime.endswith("7"):            # baslama ve bitis degerlerını sınırlandırdı 
       liste2.append(prime)               
print(liste2)                                                      # liste 2 elemanlarını yazdır
print(len(liste2))                                             # liste 2 de kac karakter oldugunu yazdırır