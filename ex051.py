import os
os.system('cls' if os.name == 'nt' else 'clear')

print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
print('   10 TERMOS DE UMA PA')
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-')
pt = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = pt + (10 - 1) * raz
for c in range(pt, dec + raz, raz):
    print(c, end = ' ')
