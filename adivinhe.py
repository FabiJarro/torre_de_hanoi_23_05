import random
movimentos = 0
n = random.randint(1,100)

while True:
        
    x = int(input('Digite sua tentativa: '))
    movimentos+=1
    if 1<x<101:

        if x<n:
            print('palpite muito baixo')

        elif x>n:
            print('palpite alto')

        else:
            print(f'vc acertou, numero de movimentos: {movimentos}')
            break

    else: 

        print('numero invalido')





