import random

palavras =['maça', 'banana', 'melancia', 'abacaxi']

palavra = random.choice(palavras)

chances = 4

certas = []

ganhou = False

print(palavra)


while True:

    letrau = str(input('entre com uma letra: '))  

    if letrau in palavra and letrau not in certas:

        certas.append(letrau)


    elif letrau not in palavra:

        chances -= 1

        print(f'chances = {chances}')
        
    ganhou = True


    for letra in palavra:

        if letra in certas:

            print(letra, end=' ')

        else: 

            print(' _ ', end=' ')
            ganhou = False
    print()

    if ganhou:
        print('GANHOU')
        break
    if chances==0:
        print('perdeu, a palavra era ', palavra)



            

