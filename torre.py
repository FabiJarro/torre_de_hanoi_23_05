
def mostrar_torres(torres):
    print("\nEstado atual:")
    for nome, pino in torres.items():
        print(f"{nome}: {pino}")


def mover(torres, origem, destino):
    if not torres[origem]:
        print("pino vazio")
        return False
    
    if torres[destino] and torres[origem][-1] > torres[destino][-1]:
        print("não se pode colocar uma peça maior sobre uma menor")
        return False
    #o -1 indica o ultimo elemento da lista, acessa?
    
    peça = torres[origem].pop() #o pop Remove de uma posição especifica, no caso o topo(o ultimo elemnto)
    torres[destino].append(peça)
    return True

def jogo():
    torres = {
        'A': [5, 4, 3, 2, 1],
        'B': [],
        'C': []
    }
    
    while torres['C'] != [5, 4, 3, 2, 1]:
        mostrar_torres(torres)
        origem = input("de qual pino você quer mover? (A, B, C): ").upper()
        destino = input("para qual pino você quer mover? (A, B, C): ").upper()

        if origem not in torres or destino not in torres:
            print("pinos inválidos. Escolha A, B ou C.")
            continue
        
        if not mover(torres, origem, destino):
            print("movimento inválido, tente novamente.")
    
    mostrar_torres(torres)
    print("Parabens, a torre está completa")

jogo()
