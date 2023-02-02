N1 = float(input('Digite a primeira nota: '))
N2 = float(input('Digite a segunda nota: '))
Média = (N1 + N2) / 2
if Média < 5:
    print('Reprovado! Sua média foi {}'.format(Média))
elif Média > 5 and Média < 6.9:
    print('Recuperação! Sua média foi {}'.format(Média))
elif Média > 7:
    print('Aprovado! Parabéns , sua média foi {}'.format(Média))
