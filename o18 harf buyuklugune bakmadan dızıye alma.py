def fonksiyon(input_str):
    char_set = set()                     # diziyi yarattık
    
    for char in input_str:    
        if char.isalnum():              # Sadece alfanumerik karakterleri kontrol et
            char_set.add(char.lower())  # Harfi küçük harfe dönüştürerek küçük/büyük harf duyarlılığını ortadan kaldır

    return len(char_set)

         # Test
input_string = "AbCdEf1234aBCdEF5678"   # dizimiz
result = fonksiyon(input_string)           # fonksiynumuz
print("Farklı harf ve rakam sayısı:", result)   # deger sayısını yazdırma





