import random  # random sayı uretme fonksiyonunu taımladık

sayilar = random.sample(range(-100,100),10)  # -100 ve 100 arasında 10 tane rastgele sayı alacak
sayilar.sort(reverse=False)                  # sayıları false kuxukten buyuge sıralar true buyukten kucuge
print("buyukten kucuge",sayilar) 




