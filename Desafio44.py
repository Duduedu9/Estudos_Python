print('{:=^40}'.format('LOJÃO DO DUDU'))
preço=float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO    
[ 1 ] Á vista dinheiro/ cheque
[ 2 ] Á vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção? '))
if opção ==1:
    total=preço-(preço*10/100)
elif opção ==2:
    total=preço -(preço*5/100)
elif opção ==3:
    total = preço
    parcela = total / 2
    print(('Sua compra será parcelada em 2x de {:.2f} Sem juros'.format(parcela)))
elif opção==4:
    total=preço+(preço*20/100)
    totparc=int(input('Quantas parcelas? '))
    parcela = total/totparc
    print(' Sua compra será parcelada em {}x de R${:.2f} Com juros'.format(totparc, parcela))
else:
    total=0
    print('\033[0;31;40mOPÇÃO INVALIDA de pagamento. Tente novamente')
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final '.format(preço,total))

