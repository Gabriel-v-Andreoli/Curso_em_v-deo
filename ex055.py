import os
os.system('cls' if os.name == 'nt' else 'clear')

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior e menor pesos apresentados foram respectivamente {:.2f} KG e {:.2f} KG'.format(maior, menor))
