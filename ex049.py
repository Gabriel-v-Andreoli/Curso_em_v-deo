import os
os.system('cls' if os.name == 'nt' else 'clear')

print('Tabuada 2.0')
n = int(input('A tabuada do número você deseja ver: '))
print('-=-=-=--=-=-=-=-=-=-=-=-=-=-')
for c in range(1, 11):
    print('{} X {} = {}'.format(n, c, n*c))
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
