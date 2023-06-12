import random

def jogar():

    imprime_mensagem_abertura()

    palavra_secreta = gera_palavra_secreta()

    letras_acertadas = inicializa_slots_letras(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erro = 0


    #enquanto (True)
    while (not enforcou and not acertou):

        jogada = request_jogada()

        if (jogada in palavra_secreta):
            marca_jogada_correta(jogada, letras_acertadas, palavra_secreta)
        else:
            erro += 1
            desenho_forca(erro)

        enforcou = erro == 7
        acertou = '_' not in letras_acertadas

        print(letras_acertadas)

    if (acertou):
        imprime_mensagem_vencedor(palavra_secreta)
    elif (enforcou):
        imprime_mensagem_perdedor(palavra_secreta)

#----------------------------------------------------------------------- ! -------------------------------------------------------------------------------

#define o caractere do campo da palavra secreta
def inicializa_slots_letras(palavra):
    return ['_' for letra in palavra]

#exibição
def imprime_mensagem_abertura():
    print('*****************************************')
    print('*******Bem vindo ao jogo da Forca********')
    print('*****************************************')

#cria uma palavra aleatoria
def gera_palavra_secreta():
    arquivo = open('palavra.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

#pede uma letra
def request_jogada():
    jogada = input('Digite uma letra:')
    jogada = jogada.strip().upper()
    return jogada

#marca a letra correta na palavra secreta
def marca_jogada_correta(jogada, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (jogada == letra):
            letras_acertadas[index] = letra
        index += 1

#mensagem do fim
def imprime_mensagem_perdedor(palavra_secreta):
    print("Você errou!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \    ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXXX     XXXX   |      ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor(palavra_secreta):
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenho_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if (__name__ == '__main__'):
    jogar()