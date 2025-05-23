import random

n = random.randint(1,100)
x = int(input('Digite sua tentativa: '))

if 1<x<100:

    if x==n:
        print('Acertou! o numero adivinhado foi', n)

    elif x<n:
        print('palpite muito baixo')
    else:
        print('palpite alto')
    print(f'seu palpite:{x}, numero:{n}')

else: 
    print('numero invalido')