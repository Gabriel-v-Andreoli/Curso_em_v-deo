import os
os.system('cls' if os.name == 'nt' else 'clear')

soma = 0
cont = 0
for c in range (1, 501):
    if c % 3 == 0:
        if c % 2 == 1:
            cont += 1
            soma += c
print('A soma de todos os {} valores é {}'.format(cont, soma))
