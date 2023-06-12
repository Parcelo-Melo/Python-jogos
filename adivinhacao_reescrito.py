import random

print('**********************************')
print('*Bem-vindo ao jogo de adivinhação*')
print('**********************************')

numero_secreto = (random.randrange(1,11))
total_tentativas = 0
pontos = 100

print('Em que nível você quer jogar?')
print('(1) Fácil || (2) Médio || (3) Dificíl')

nivel = int(input('Escolha seu nível: '))

if (nivel == 1):
    total_tentativas = 5
elif (nivel == 2):
    total_tentativas = 3
elif (nivel == 3):
    total_tentativas = 2

for rodada in range(1, total_tentativas + 1):
    print('Rodada {} de {}' .format(rodada, total_tentativas))
    jogada_str = input('Digite um número: ')
    jogada = int(jogada_str)


    menor = jogada < numero_secreto
    maior = jogada > numero_secreto
    acerto = jogada == numero_secreto

    if (jogada < 1 or jogada > 10):
        print('Digite um número valído!')
        continue

    print('Você digitou: {}' .format(jogada))
    if (acerto):
        print('E acertou!')
        print('Sua pontuação foi: {}' .format(pontos))

        break
    else:
        if (menor):
            print('Você errou! a sua jogada foi menor que o numero secreto.')
            pontos = pontos - 25
            print('Sua pontuação: {}' .format(pontos))
        elif (maior):
            print('Você errou! a sua jogada foi maior que o número secreto.')
            pontos = pontos - 25
            print('Sua pontuação: {}' .format(pontos))

num_reveal = int(input('Quer revelar o número secreto? (1 = sim || 0 = não): '))
if (num_reveal == 1):
    print('O número secreto é: {}' .format(numero_secreto))
print('Fim do jogo!')

