import math
CO = float(input('Qual o Cateto Oposto?: '))
CA = float(input('Qual o Cateto Adjacente?: '))
HI= math.hypot(CO,CA)
print('A hipotenusa vai medir {:.2f}'.format(HI))