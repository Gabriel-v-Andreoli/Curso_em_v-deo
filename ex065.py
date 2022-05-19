import os
os.system('cls' if os.name == 'nt' else 'clear')

                #variáveis
soma = 0
cont = 0
maior = 0
menor = 0
while True:
    try:    #forma que eu encontrei pra parar o programa sem ter que digitar um número especifico 
        n = int(input('informe um número (para encerrar o programa deixe em branco): '))
        soma += n
        cont += 1
        if cont == 1: #definir um maior e um menor para subistituir o zero na variável
            maior == n
            menor == n
        else: #redefinir o maior e menor de acordo com os números já inseridos no programa pelo usuário 
            if n > maior:
                maior = n
            elif n < menor:
                menor = n

    except: #  fim / repetição
        print('a média é: ', soma/cont)
        print(f'O maior número é {maior}\nO menor número é {menor}')
        a = str(input('Deseja adicionar mais números [S/N]: ')).upper().strip()
        if a != 'S':
            break
