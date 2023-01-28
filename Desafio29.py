vel=float(input('Qual a velocidade do carro? '))
Lim=int(input('Qual o Limite de velocidade? '))
LV=vel-Lim
Multa=(7*LV)
if vel > Lim:
    print('Você recebeu uma multa de {} R$'.format(Multa))
else:
    print('Você não ultrapassou o limite de velocidade')