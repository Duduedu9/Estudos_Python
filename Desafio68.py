import random
import time

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
vezes_acertos = 0
while True:
    pc = random.randint(0, 10)
    pi = str(input('Par ou Ímpar [P / I]: ')).upper()
    while pi != 'P' and pi != 'I':
        pi = str(input('Par ou Ímpar [P / I]: ')).upper()
    n = int(input('Diga um valor: '))
    soma = pc + n
    if pi == 'P' and soma % 2 == 0:
        vezes_acertos += 1
        print(f'{"_"*50}\nVocê jogou {n} e a maquina jogou {pc}. Total é {soma}. DEU PAR.\n{"-"*50}')
        print(f'VOCÊ VENCEU!\nVamos jogar novamente...\n{"-="*20}')
        time.sleep(1)
    if pi == 'P' and soma % 2 == 1:
        print(f'{"_"*50}\nVocê jogou {n} e a maquina jogou {pc}. Total é {soma}. DEU IMPAR.\n{"_"*50}')
        print(f'VOCÊ PERDEU!\nGAME OVER\n{"-="*20}')
        print(f'Você Venceu {vezes_acertos} vezes.')
        break
    if pi == 'I' and soma % 2 == 1:
        vezes_acertos += 1
        print(f'{"_"*50}\nVocê jogou {n} e a maquina jogou {pc}. Total é {soma}. DEU IMPAR.\n{"_"*50}')
        print(f'VOCÊ VENCEU!\nVamos jogar novamente...\n{"-="*20}')
        time.sleep(1)
    if pi == 'I' and soma % 2 == 0:
        print(f'{"_"*50}\nVocê jogou {n} e a maquina jogou {pc}. Total é {soma}. DEU PAR\n{"_"*50}')
        print(f'VOCÊ PERDEU!\nGAME OVER\n{"-="*20}')
        print(f'Você Venceu {vezes_acertos} vezes.')
        break



