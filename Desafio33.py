n1=int(input('Leia o primeiro numero: '))
n2=int(input('Leia o segundo numero: '))
n3=int(input('Leia o terceiro numero: '))
Menor= n1
Maior= n1
if n2 > Maior:
   Maior = n2
if n3 > Maior:
   Maior=n3

if n2 < Menor:
    Menor =n2
if n3 < Menor:
    Menor=n3

print('O menor numero é {}'.format(Menor))
print('O maior numero é {}'.format(Maior))
