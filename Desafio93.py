jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range (0,tot):
    partidas.append(int(input(f'Quantas gols na partida {c}? ')))
jogador['gols']= partidas [:]
jogador['total']= sum(partidas)
print('=-'*30)
print(jogador)
for k, v in jogador.items():
    print(f' O campo {k} tem valor {v}')
print('=-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador["gols"]):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um tootal de {jogador["total"]} gols')

