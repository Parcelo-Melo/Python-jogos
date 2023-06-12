import random

def jogar():

    print('**********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('**********************************')

    numero_secreto = (random.randrange(1, 11))
    total_tentativas = 0
    pontos = 100

    print('Em qual nível você deseja jogar?')
    print('(1) Fácil || (2) Médio ||  (3) Difícil')

    nivel = int(input('Defina o nível: '))

    if (nivel == 1):
        total_tentativas = 5
    elif (nivel == 2):
        total_tentativas = 3
    elif (nivel == 3):
        total_tentativas = 2

    for rodada in range(1, total_tentativas + 1):
        print('Rodada {} de {}' .format(rodada, total_tentativas))
        jogada_str = input('Digite um número entre 1 e 10: ')
        jogada = int(jogada_str)

        acerto = jogada == numero_secreto
        maior = jogada > numero_secreto
        menor = jogada < numero_secreto

        if (jogada < 1 or jogada > 10):
            print('Digite um número dentro do range permitido!')
            continue

        print('Você digitou:', jogada)
        if (acerto):
            print('E acertou!')
            break
        else:
            if (maior):
                rint('Você errou! A sua jogada foi maior que o número certo')
                pontos_perdidos = 25
                pontos = pontos - pontos_perdidos
                print('Seus pontos estão em: {}'.format(pontos))
            elif (menor):
                print('Você errou! A sua jogada foi menor que o número certo')
                pontos_perdidos = 25
                pontos = pontos - pontos_perdidos
                print('Seus pontos estão em: {}' .format(pontos))


    print('Fim do jogo.')
    print('Sua pontuação foi de {}' .format(pontos))
    num_reveal = int(input('Quer revelar o número secreto? (1 = sim || 0 = não): '))
    if (num_reveal == 1):
        print('O número secreto é: {}' .format(numero_secreto))
        return

if (__name__ == '__main__'):
    jogar()







