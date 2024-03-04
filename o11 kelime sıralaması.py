
 
firstwords = input("please write your words =")     # kullanıcıdan deger alma
secondwords = input("please write your words =")

birleşikkelime = firstwords+secondwords  # kelimeleri birleştirdik
birleşikkelime = ''.join(sorted(birleşikkelime))  # birleşik kelimeyı alfebetık sekilde sıraladı 


print("firstwords is ",firstwords)      # aldıgımız degeri yazdırma
print("secondwords is",secondwords)
print("combinations is",birleşikkelime)

