DistanciaKm=int(input('Qual a distancia em Km? '))
Passagem:float= 0.50*DistanciaKm
Passagem200:float=0.45*DistanciaKm
if DistanciaKm < 200:
    print('A sua passagem de ônibus custou {}'.format(Passagem))
else:
    print('A sua passagem de ônibus custou {}'.format(Passagem200))
