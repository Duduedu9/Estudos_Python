n=s=vd=0
while True:
    n=int(input('DIgite um numero [999 para parar] '))
    if n == 999:
        break
    s+=n
    vd+=1

print(f'Foram digitados {vd} numeros e a soma entre eles é {s} ')