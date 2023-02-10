from time import sleep
M=0
S=0
maior=0
n1=int(input('Leia o primeiro numero: '))
n2=int(input('Leia o segundo numero: '))
opção=0
while opção!= 5:
    print('''Menu Curso em Video
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NUMEROS
    [ 5 ] SAIR DO PROGRAMA''')
    opção=int(input('Qual a sua opção? '))
    if opção == 1:
      S= n1+n2
      print(' A soma entre {} e {} é {}'.format(n1, n2, S))
    elif opção == 2:
        M=n1*n2
        print('O resultado de {} x {} é igual a {}'.format(n1, n2, M ))
    elif opção ==3:
            if n1 > n2:
                maior = n1
            if n2 > n1:
                maior = n2
            print('Entre {} e {} o maior numero é {}'.format(n1, n2, maior))
    elif opção ==4:
        print('Informe os numeros novamente. ')
        n1=int(input('Primeiro valor: '))
        n2=int(input('Segundo valor: '))

    elif opção ==5:
        print('Finalizando....')
    else:
        print('Opção Invalida, tente novamente ')
    print('=-='*10)
    sleep(2)
print('FIm do programa. Volte sempre! ')