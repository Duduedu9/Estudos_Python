Peso=float(input('Qual seu peso? '))
Altura=float(input('Qual sua altura? '))
Imc=Peso/Altura**2
if Imc < 18.5:
    print('Você está com IMC {}, abaixo do peso'.format(Imc))
elif Imc >= 18.5 and Imc <25:
    print('Você está no peso ideial ,IMC {}'.format(Imc))
elif Imc <= 25 and Imc <30:
    print('Você está com sobrepeso, {}'.format(Imc))
elif Imc <=30 and Imc <40:
    print('Você está Obeso, IMC {}'.format(Imc))
elif Imc >=40:
    print('Obesidade Morbida, seu IMC é {}'.format(Imc))
