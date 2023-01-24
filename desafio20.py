import random
Al1=(input('Primeiro aluno: '))
Al2=(input('Segundo aluno: '))
Al3=(input('Terceiro aluno: '))
Al4=(input('Quarto aluno'))
Lista=[Al1, Al2, Al3, Al4]
random.shuffle(Lista)
print('A ordem dos alunos sorteados foi {}'.format(Lista))