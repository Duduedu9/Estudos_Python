Lista= []
for c in range (0, 5):
    n= int(input('Digite um valor: '))
    if c == 0 or n > Lista[-1]:
        Lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos=0
        while pos < len(Lista):
            if n<= Lista[pos]:
                Lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram {Lista}')