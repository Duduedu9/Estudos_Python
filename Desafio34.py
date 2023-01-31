Sal=int(input('Qual o Salario do funcionario? '))
print(Sal)
NSal1=Sal+10/ 100*Sal
NSal2=Sal+15/ 100*Sal
if Sal > 1250 :
    print('Seu novo salario será de {}'.format(NSal1))
else:
    print('Seu novo Salario será de {}'.format(NSal2))
