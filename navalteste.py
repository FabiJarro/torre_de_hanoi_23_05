import random

def criar_tab():
    return[[" -" for _ in range(10)] for _ in range(10) ]

def imprime_tabuleiro(tabuleiro):
    print("  "+ "  ".join(str(i) for i in range(10)))
    for i, linha in enumerate(tabuleiro):
        print(f'{i}'+" ".join(linha))

#literalmente numera

tabuleiro=criar_tab()

tamanhos = [4, 3, 3, 2]
#tipo, um navio de tamanho 4; 3 tals

def navios(tabuleiro, tamanhos):
    for tamanho in tamanhos:
        colocado=False
        while not colocado:
            sentido=random.choice([' H',' V'])

            if sentido==' H':
                linha=random.randint(0,9)
                coluna=random.randint(0,10-tamanho)

                if all(tabuleiro[linha][coluna+i]== ' -' for i in range(tamanho)):
                    for i in range (tamanho):
                        tabuleiro[linha][coluna+i]=' N'
                    colocado=True
            else:
                linha=random.randint(0,10-tamanho)
                coluna=random.randint(0,9)

                if all(tabuleiro[linha+i][coluna] == ' -' for i in range(tamanho)):
                    for i in range(tamanho):
                        tabuleiro[linha+i][coluna]=' N'
                    colocado=True

tabuleiro_navios=criar_tab()
tabuleiro_exibicao = criar_tab()

navios(tabuleiro_navios, tamanhos)
#imprime_tabuleiro(tabuleiro)

def tiros(tabuleiro_navios, tabuleiro_exibicao):
    
    linha= int(input("linha q deseja atacar(0-9):"))
    coluna=int(input("coluna q deseja atacar(0-9):"))
    
    if tabuleiro_navios[linha][coluna]==' N':
        print("acertouu")
        tabuleiro_exibicao[linha][coluna]=' X'
        
    elif tabuleiro_navios[linha][coluna] == ' -':
        print("na agua")
        tabuleiro_exibicao[linha][coluna] = ' O'
        
    elif tabuleiro_exibicao[linha][coluna] in [' X', ' O']:
        print("vc já atirou aqui")
    # else:
        # print("Posição invalida")


def ainda_navios(tabuleiro):
    for linha in tabuleiro:
        if ' N' in linha:
            return True
    return False

while ainda_navios(tabuleiro_navios):
    print("")
    imprime_tabuleiro(tabuleiro_exibicao)
    tiros(tabuleiro_navios, tabuleiro_exibicao)
print("Parabens!!! vc afundou todos os navios ")




            


