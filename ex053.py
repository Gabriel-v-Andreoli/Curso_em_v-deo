import os
os.system('cls' if os.name == 'nt' else 'clear')

print('=' * 25)
print('Detector de palíndromos')
print('=' * 25)
frase = str(input('Digite algo: ')).upper().strip()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print('A frase {} fica {} ao contrario, por tanto'.format(frase, inverso), 'é um palíndromo' if inverso == frase else 'não é um palíndromo')
