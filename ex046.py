import os
import time
os.system('cls' if os.name == 'nt' else 'clear')

print('Iniciar contagem regressiva?(S/N)')
resposta = str(input('Resposta: ')).lower()
if resposta == 's':
    for c in range(10, 0, -1):
        print(c)
        time.sleep(1)
elif resposta == 'n':
    print('OK')
else:
    print('Opção invalida')
