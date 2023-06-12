import random

print('***********************************')
print('****Bem vindo ao jogo da Forca!****')
print('***********************************')

arquivo = open('palavra.txt', 'r')
palavras = []

for linha in arquivo:
    linha = linha.strip()
    palavras.append(linha)

arquivo.close()

numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()
slots = ['_' for letra in palavra_secreta]

enforcou = False
acertou = False
erros = 0

print(slots)

while(not enforcou and not acertou):
    jogada = input('Digite uma letra: ')
    jogada = jogada.strip().upper()

    if(jogada in palavra_secreta):
        index = 0
        for letra in palavra_secreta:
            if (jogada.upper() == letra.upper()):
                slots[index] = letra
            index += 1
    else:
        erros += 1
        print('restam', erros - 6)

    enforcou = erros == 6
    acertou = '_' not in slots
    print(slots)

    if(acertou):
        print('Você ganhou!')
    elif(enforcou):
        print('Você perdeu!')




