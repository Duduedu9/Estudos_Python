ValorCasa=float(input('Qual o valor da casa?: R$ '))
Sal=float(input('Qual o Salario do comprador?: R$ '))
Tfinanciamento=int(input('Qual o tempo do financiamento? '))
Pmensal = ValorCasa/(Tfinanciamento*12)
minimo=Sal*30/100
print('Para pagar uma casa de R${:.2f} em  anos {}'.format(ValorCasa,Tfinanciamento))
print('A prestação será de R$ {:.2f}'.format(Pmensal))
if Pmensal <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo negado !')
