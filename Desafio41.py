from datetime import date
atual=date.today().year
Nasc=int(input('Qual seu ano de nascimento? '))
Idade= atual-Nasc
if Idade <= 9:
    print('Atleta tem {} anos, e é da categoria Mirim!'.format(Idade))
elif Idade <= 14:
    print('Atleta tem {} anos, e é da categoria Infantil'.format(Idade))
elif Idade <=19:
    print(' Atleta tem {} anos, e é da categoria Junior'.format(Idade))
elif Idade <=25:
    print('Atleta tem {} anos. e é da categoria Senior'.format(Idade))
elif Idade >25:
    print('Atleta tem {} anos, e é da categoria Master'.format(Idade))
