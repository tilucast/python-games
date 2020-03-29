import random


def forca():

    print_hello()

    palavra_secreta = gerar_palavra_secreta()

    letras_acertadas = print_letras_acertadas(palavra_secreta)

    print(f'{letras_acertadas}, A palavra tem {len(letras_acertadas)} letras. ')

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input('Chute uma letra da palavra: ').lower().strip()

        if(chute in palavra_secreta):
            verificar_chute(chute, palavra_secreta, letras_acertadas)
            acertou = '_' not in letras_acertadas
        else:
            erros += 1
            enforcou = erros == 6

        print(letras_acertadas)
        print(f'você tem {6 - erros} tentativas')

    print('você ganhou.') if acertou == True else print('você perdeu.')
    print(f'Fim do jogo! A palavra secreta era "{palavra_secreta}".')


def print_hello():
    print('***************************')
    print('Bem vindo ao jogo de Forca!')
    print('***************************')


def gerar_palavra_secreta(nome_arquivo="palavras.txt"):
    with open(nome_arquivo, encoding="utf-8") as arquivo:
        palavras = []
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras))
    return palavras[numero].lower()


def print_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def verificar_chute(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra

        index += 1


if(__name__ == "__main__"):
    forca()
