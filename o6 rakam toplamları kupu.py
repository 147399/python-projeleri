
# 3 basamaklı sayıların kac tanesi rakamlarının toplamının kupune eşıttır

liste = []                        # sayıları  icine eklıcegımız lıste 
for sayi in range(100,1000):      # sayılar 100 ile 999 arasından secılecek
    toplam = 0
    gecici_sayi = sayi
    while gecici_sayi!= 0:          # sayı 0 olmadıgı surece
        basamak = gecici_sayi %10   # sayının 10 ıle bolumunden kalan 1 ler basamagı
        toplam  += basamak  ** 3      # basamagın 3. kuvvetı  
        gecici_sayi //= 10           # gecici sayıyı  10 bol 
    if toplam == sayi :              # toplamın  sayıya eşit  olup olmadıgını sorgular 
        liste.append(sayi)           # sayıları lısteler    
 
print(liste)