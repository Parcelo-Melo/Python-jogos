import forca
import adivinhacao

def escolher_jogo():
    print('*******************')
    print('Escolha o seu jogo!')
    print('*******************')

    print('(1) Jogo da forca || (2) Jogo de adivinhação')
    jogo = int(input('Qual jogo? '))

    if (jogo == 1):
        print('Jogando forca')
        forca.jogar()
    elif (jogo == 2):
        print('Jogando adivinhação')
        adivinhacao.jogar()

if (__name__ == '__main__'):
    escolher_jogo()