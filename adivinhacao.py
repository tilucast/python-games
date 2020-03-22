import random


def adivinhacao():
    print('Bem vindo ao jogo de adivinhação!')
    dificuldade = int(input('Digite o nível de dificuldade ( entre 1 e 3 )'))

    numero_secreto = random.randrange(1, 101)
    numero_tentativas = 0
    pontuacao = 600

    if dificuldade == 1:
        numero_tentativas = 15

    elif dificuldade == 2:
        numero_tentativas = 10

    elif dificuldade == 3:
        numero_tentativas = 5

    else:
        print('Escolha a dificuldade entre 1 e 3')

    for x in range(0, numero_tentativas):
        print(f'Tentativas restantes: {numero_tentativas}')
        print(f'Sua pontuação atual é {pontuacao}')
        chute = int(input('Digite um numero entre 1 e 100: '))

        if(chute < 1 or chute > 100):
            print('Número fora do escopo proposto.')
            numero_tentativas -= 1
            continue

        if(chute == numero_secreto):
            print('Você acertou')
            break
        else:
            if(chute > numero_secreto):
                print('Você chutou pra cima')
            elif(chute < numero_secreto):
                print('Você chutou pra baixo')
            pontuacao -= chute

        if(pontuacao <= 0):
            print('Você perdeu por zerar os pontos.')
            numero_tentativas = 0
            break

        numero_tentativas -= 1
    print(
        f'Fim do jogo!, o número era {numero_secreto}, e você acabou com {pontuacao} pontos')


if(__name__ == "__main__"):
    adivinhacao()
