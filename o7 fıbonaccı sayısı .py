#fıbonaccı sayı dizisi ilk  iki terımı 1 olan ve sonraki her terimi kendisinden oncekı 2 terimin 
# toplamı olan sayı dızısı . 1,1,2,3,5,8,13,21....


fibonacci_list = []         # fibonacci listemız 
fibonacci_list.append(1)    # listeye 1 ekledık 
fibonacci_list.append(1) 


index = 2

while True:  #sart saglandıkca calıs 
    fibonacci_list.append(fibonacci_list[index -2] +  fibonacci_list[index - 2])   # 0. ındexle 1. ındexı ekledık
    index += 1     # ındexı 1 arttırdık
    if len(fibonacci_list)  == 100:    #fıbonccı lıstesı  100 elemanlı olunca dur
       break
print(fibonacci_list)   
        



"""

FOR DONGUSU 

fibonacci_list = []         # fibonacci listemız 
fibonacci_list.append(1)    # listeye 1 ekledık 
fibonacci_list.append(1) 
 

for i in range(2,99):      # i deger aralıgını tanımladık 
    fibonacci_list.append(fibonacci_list[ i - 2] +  fibonacci_list[ i - 2])   # i -2. eleman ve i-1 . elemaın toplamını yazdırır 
print(fibonacci_list)
   
        
"""
