import random
Al1=(input(('Qual o nome do 1 aluno?')))
Al2=(input('Qual o nome do 2 aluno?'))
Al3=(input('Qual o nome 3 do aluno?'))
Al4=(input(('Qual o nome do 4 aluno?')))
Lista = [Al1,Al2,Al3,Al4]
Sorteio =random.choice(Lista)
print('O aluno sorteado foi {}'.format(Sorteio))
