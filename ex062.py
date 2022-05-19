import os
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

continuar = True
while continuar: #repetição de programa
    cls()
    t1 = int(input('Primeiro termo da P.A: '))
    r = int(input('Razão da P.A: '))
    i = 0
    print()

    while i < 10:                                   #estrutura para calcular a p.a e mostrar os termos
        i += 1                                         #indice
        print(t1, end = ' , ' if i < 10 else ' ')      #mostrar o termo da p.a
        t1 += r                                        #calculo da p.a
    print() #formatação

    while True: #adição de termos
        x = str(input('Dejesa mais termos [S/N]: ')).strip().upper()
        if x == 'S':
            y = int(input('Quantos: '))

            while y > 0:
                print(t1)
                t1 += r
                y += -1
        elif x == 'N':
            break
        else:
            print('Opção inválida')

    rep = str(input('Repetir programa: ')).upper().strip()

    if rep == 'S':
        continue
    elif rep == 'N':
        continuar = False
    else: 
        print('Opção inválida')
