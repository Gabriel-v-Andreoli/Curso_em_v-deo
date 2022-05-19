import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()

                #minha tentativa
'''
conti = True
while conti:
    sexo = str(input('Qual é o seu sexo [M/F]: ')).upper().strip()
    print(f'entrada: {sexo}')
    if (sexo == 'F') or (sexo == 'M'):
        print('\033[32mVálido! :)\033[m')
        conti = False
    else:
        print('\033[31minválido!!!  :(\033[m')
        '''

            #outra forma de resolver
sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Digite um sexo válido [M/F]: ')).strip().upper()[0]
print('Válido')