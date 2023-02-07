Soma=0
cont=0
for c in range (1, 7):
    n=int(input('Digite um numero: '))
    if n % 2==0:
        Soma +=n
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont,Soma))
