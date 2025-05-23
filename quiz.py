perguntas = [
    ('O brasil é o unico pais que tem a floresta amazonica?', 'F'),
    ('O brasil é o unicos pais que fala portugues: ', 'F'),
    ('O ponto mais alto do Brasil é o pico da neblina', 'V'),
    ('A pele é o maior orgão do corpo humano? ', 'V'),
    ('O sol é uma estrela? ', 'V')
]

def quiz():
    pontuação = 0
    for pergunta, resposta in perguntas:
        resposta_usuario = str(input('Digite V ou F para cada pergunta')).isupper()
        if resposta_usuario == resposta:
            print('Resposta certa')
            pontuação +=1
        else:
            print('Resposta incorreta')   
    print('sua pontuação: ', pontuação)


quiz()