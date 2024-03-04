def maskele(text):  # maskelene işlemini yapacak fonksiyon


    # Text uzunluğunu hesapla

    text_length = len(text)

    # Son dört karakter dışındaki karakterleri '#' ile değiştir
    masked_text = '#' * (text_length - 4) + text[-4:]

    return masked_text

original_text = input("whats your password :")  # kullanıcıda şifresini alır 
masked_result = maskele(original_text)        # şifreyi maskeli halini yazdırır
print(masked_result)



for _ in range(100):    # 100 kere a harfini yan yana yazdırır
   print("a")



def maskele(text):
    textuzunlugu = len(text) 
    maskedtext = "*" * (textuzunlugu+4) + text[-2:]   # sıfrenın son ıkı hane dısındakı degerleri * isareti koyma
    return maskedtext
originaltext = input("şifreniz :")            #degerlerimiz yazdırma
maskedresult = maskele(originaltext)
print(maskedresult)



