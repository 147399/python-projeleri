import random

liste = ["ankara" ,"mersin","istanbul","uzum","türkiye","adana","bilgisayar"]

Kelime = random.choice(liste)

adam = ["""
   +----+     
   o    |
  /|\   |
  / \   |
       -----
        ""","""
   +----+     
   o    |
  /|\   |
  /     |
       -----        
        ""","""
   +----+     
   o    |
  /|\   |
        |
       -----        
        ""","""
   +----+     
   o    |
  /|    |
        |
       -----        
        ""","""
   +----+     
   o    |
  /     |
        |
       -----       
        ""","""
    +----+     
   o    |
        |
        |
       -----        
        ""","""
    +----+     
        |
        |
        |
       -----        
        """]

dogruHarf = []
yanlısHarf = []
hak = len(adam)

while hak > 0 :
    out = ""
    for h in Kelime :
        if h in dogruHarf :
            out += h 
        else:
            out += "_"
    if out == Kelime :
        break 
    print("kelime: ",out)
    print(adam[hak-1])
    girHarf = input()
    if girHarf in dogruHarf or girHarf in yanlısHarf:
        print(girHarf,"zaten girildi")
    elif girHarf in Kelime :
        print("dogru harf")
        dogruHarf.append(girHarf)
    else :
        print("Yanlış harf..!")
        hak -= 1
        yanlısHarf.append(girHarf)
if hak != 0 :
    print("tebrikler kazandınız . Kelimeniz : ",Kelime)
else :
    print("Maalesef kaybettiniz . Kelime :",Kelime ,"ydi")






    
