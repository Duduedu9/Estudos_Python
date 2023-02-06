from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador=randint(0,2)
print(''' Suas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura ''')
jogador=int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*11)
if computador==0: #Computador Jogou pedra
    if jogador==0:
        print('EMPATE')
    elif jogador ==1:
        print('JOGADOR VENCE')
    elif jogador==2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Invalida')
elif computador ==1:#Computador jogou papel
    if jogador==0:
        print('COMPUTADOR VENCE')
    elif jogador ==1:
        print('EMPATE')
    elif jogador==2:
        print('JOGADOR VENCE')
    else:
        print('Jogada Invalida')
elif computador ==2: #Computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
     print('COMPUTADOR VENCE')
    elif jogador == 2:
     print('EMPATE')
    else:
        print('Jogada Invalida')