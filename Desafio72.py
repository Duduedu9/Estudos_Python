cont= ('zero', 'Um', 'Dois', 'Três', 'Quatro',
          'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
          'Dez', 'Onze', 'Doze', 'Treze', 'Cartoze',
          'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
          'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um numero entre 0 e 20 : '))
    if 0 <=  n <=20:
        break
    print('Tente novamente!')
print(f'O numero digitado foi {cont[n]}')