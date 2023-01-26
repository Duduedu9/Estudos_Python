from random import randint
computador= randint(0,5)
print('-=-'*20)
print('vou pensar em um numero entre 0 e 5. Tente advinhar...')
print('-=-'*20)
jogador= int(input('Em que numero eu pensei? '))
if jogador== computador:
    print('Parabéns, você conseguiu me vencer')
else:
    print('Ganhei, Eu pensei no numero {} e nao no {}'.format(computador,jogador))