import os
os.system('cls' if os.name == 'nt' else 'clear')

n = int(input('Digite um número: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont += 1
        print('\033[32m', end = ' ')
    else:
        print('\033[31m', end = ' ')
    print( '{}'.format(c), end=' ')
print('\033[m')
print('O número {} é divisivel por {} números, por tanto'.format(n, cont), 'é primo' if cont == 2 else 'não é primo')
