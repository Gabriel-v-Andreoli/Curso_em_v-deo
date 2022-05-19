import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

conti = True
while conti:
    # Números
    cls()
    n1 = float(input('Digite um número: '))
    n2 = float(input('Digite outro: '))

    while True: # opções
        print('[1] somar \n[2] multiplicar \n[3] maior \n[4] novos números \n[5] sair do programa')
        user = int(input('Sua escolha: '))
        if (user == 1):
            print(f'{n1} + {n2} = {n1 + n2}')
        elif (user == 2):
            print(f'{n1} x {n2} = {n1 * n2}')
        elif (user == 3):
            if (n1 > n2):
                maior = n1
            elif (n2 > n1):
                maior = n2
            print(f'O maior número é {maior}')
        elif (user == 4) or (user == 5):
            break
    if (user == 5):
        conti = False
