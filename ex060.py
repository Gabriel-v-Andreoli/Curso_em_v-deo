import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


cls()
print('=' * 30)
print('Calculo de Fatorial')
print('=' * 30)
print()
fat = int(input('Número: '))
print(f'{fat}! ->', end = ' ')
print(f'{fat} x', end = ' ')
resultado = 1
while fat > 1:
    resultado *= fat
    fat += -1
    print(f'{fat}', end = ' x ' if fat > 1 else ' = ')
print(resultado)
