# Outras loterias além da megasena

# lotomania -> escolher 50 números entre 0 e 99 (range será 0, 99 + 1)
# lotofacil -> escolher 15 números entre 1 e 25 (range será 0, 25 + 1)

import random

gerados = list()
cont = 0
while True:
    n = random.randint(0, 99 + 1)
    if n not in gerados:
        gerados.append(n)
        cont += 1
        if cont >= 50:
            break

emordem = sorted(gerados)

print('-' * 39)
print('NÚMEROS GERADOS:'.center(39))
print('-' * 39)
for i in range(0, len(emordem)):
    print(f'{emordem[i]:3}', end = ' ')
    if (i + 1) % 10 == 0:
        print()

