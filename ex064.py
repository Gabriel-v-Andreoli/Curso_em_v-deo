import os
os.system('cls' if os.name == 'nt' else 'clear')


cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n != 999: #flag
        soma += n
        cont += 1
    else: #parar o programa
        break
print(f'foram informados {cont} números')
print(f'A soma dos números é {soma}')