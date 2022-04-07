import os
os.system('cls' if os.name == 'nt' else 'clear')

maior_i = 0
nome_v = ''
soma_idade = 0
soma = 0
for c in range(1, 5):
    print('================= {}ª ================'.format(c))
    nome = str(input('Nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Sua idade: '))
    sexo = str(input('Sexo (M/F): ')).strip().upper() 
    if c == 1 and sexo == 'M':
        maior_i = idade
        nome_v = nome
    if sexo == 'M' and idade > maior_i:
        maior_i = idade
        nome_v = nome
    if sexo == 'F':
        if idade < 20:
            soma +=1
    soma_idade += idade
media = soma_idade/c
print('A média das idades do grupo é {}'.format(media))
print('O homem mais velho se chama {} e tem {} anos'.format(nome_v, maior_i))
print('Tem {} mulheres abaixo de 20 anos'.format(soma))
