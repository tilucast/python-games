import forca
import adivinhacao


def escolhe_jogo():
    jogo_escolhido = int(input(
        'Escolha qual jogo quer jogar: (1) Forca ou (2) Adivinhação ...'))

    if(jogo_escolhido == 1):
        print('Jogando Forca')
        forca.forca()
    else:
        print('Jogando Adivinhação')
        adivinhacao.adivinhacao()


escolhe_jogo()
