n=c=0
while True:
     n=int(input(' Quer ver a tabuada de qual valor? '))
     if n < 0:
         break
     for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n*c))
print('PROGRAMA TABUADA ENCERRADO')

