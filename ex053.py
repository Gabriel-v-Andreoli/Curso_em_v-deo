import os
os.system('cls' if os.name == 'nt' else 'clear')


print('='*30)
print('Detector de palíndromos')
print('='*30)
frase = str(input('Digite uma frase: ')).upper().strip()
separado = frase.split()
# junto é uma lista, ent da pra colocar que o contrario recebe o junto na posição c
junto = ''.join(separado)
contrario = ''
for c in range(len(junto) -1, -1, -1):
    contrario += junto[c]
print(f'A frase {frase} ao contrário fica {contrario}, logo', end = ' ')
if junto == contrario:
    print('é um palíndromo')
else:
    print('não é um palíndromo')
