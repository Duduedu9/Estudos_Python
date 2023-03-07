valores= []
for cont in range (0,5):
    valores.append(int(input(f'Digite um valor para posição {cont}:')))
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)}')
print(f'O menor valor digitado foi {min(valores)}')