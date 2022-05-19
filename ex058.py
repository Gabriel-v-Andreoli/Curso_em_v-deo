import os
from time import sleep
import random 
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


rep = True
while rep:
    cls()
    pc = random.randint(1,5)
    cont = 0
    lista = []
    def contador():
        print(f'Tentativas necessárias: {cont}')
    con = True
    while con:
        cls()
        print('-'*30)
        print('Jogo de advinhanhação')
        print('-'*30)
        print('O pc escolheu um número aleatório de 1 a 5')
        print('Números já utilizados: ', lista)
        cont += 1
        user = int(input('Qual você acha que foi: '))
        contador()
        lista.append(user)
        sleep(1)
        if user == pc:
            print('\033[mParabéns')
            con = False
    re = str(input('Jogar dnv? [S/N]: ')).strip().upper()
    if re == 'S':
        continue
    elif re == 'N':
        rep = False
    else:
        print('Opção inválida')
        rep = False
