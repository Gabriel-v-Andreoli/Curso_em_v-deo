import os
os.system('cls' if os.name == 'nt' else 'clear')

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Número: '))
    if c % 2 == 0:
        cont += 1
        soma += c
print('Foram indicados {} números pares e a soma deles é {}'.format(cont, soma))
 