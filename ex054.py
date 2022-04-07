import os
from datetime import date
os.system('cls' if os.name == 'nt' else 'clear')

ano_atual =  date.today().year
menor = 0
maior = 0
for c in range(7):
    nascimento = int(input('Ano de nascimento da {}ª pessoa: '.format(c + 1)))
    if ano_atual - nascimento < 18:
        menor += 1
    else:
        maior += 1
print('Das 7 pessoas {} são maiores de idade e {} são menores'.format(maior, menor))
