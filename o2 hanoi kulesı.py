


"""

n: disk sayısı,
 s: kaynak,
 t: hedef,
 b: tampon

"""


def hanoi(n, s, t, b):   # degisken tanımlama
    assert n > 0   # n 0 dan buyuk olsun
    if n == 1:  #n 1 e esitse deger degıstırme     
        print('move', s, 'to', t)   # s ten t ye blok tasıma
    else:
        hanoi(n - 1, s, b, t)   # hanoi kulesi denklemi  her taşı bir bir oynat 
        hanoi(1, s, t, b)
        hanoi(n - 1, b, t, s)


if __name__ == '__main__':
    hanoi(1, 6, 1, 1) 
