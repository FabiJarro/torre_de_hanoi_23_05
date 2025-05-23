import random

acertos=1

while True:

    escolha = ['papel', 'pedra', 'tesoura']
    c = random.choice(escolha)
    x = str(input('Pedra, papel ou tesoura ou sair? '))


    if x == 'pedra' or x== 'papel' or x=='tesoura' or x=='sair':

        if x=='sair':
            break

        if x==c:
            print(f'computador:{c}, sua escolha {x}, EMPATE!')

        elif x=='pedra' and c=='papel' or x=='papel' and c=='tesoura' or x=='tesoura' and c=='pedra':
            print(f'perdeu! computador:{c}, sua escolha: {x} ')
        else:
            print(f'ganhou! computador:{c}, sua escolha: {x}, acertos = {acertos} ')
            acertos+=1
    else:
        print('invalido')
    
    if x=='sair':
        break
