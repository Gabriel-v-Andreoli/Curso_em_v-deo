import os
os.system('cls' if os.name == 'nt' else 'clear')

cont = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end = ' ')
        cont += 1
    else:
        print('\033[31m', end = ' ')
    print(c, end = ' ')
print('\033[m')
print('O número {} é divisível por {} números, por tanto'.format(num, cont), 'é primo' if cont == 2 else 'não é primo')
