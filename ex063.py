import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

cls()
n = int(input('Digite um número: '))
sequencia = [0, 1]
t1 = 0
t2 = 1
t3 = 0
if n > 2:
    repetições = n - 2
    while repetições > 0:
        t3 = t1 + t2
        sequencia.append(t3)
        t1 = t2
        t2 = t3
        repetições += -1
elif n == 2:
    print('Os dois primeiros termos da sequência de fibonacci são:',sequencia)
elif n == 1:
    for c in range (1):
        print('O primeiro termo da sequência de fibonacci é :',sequencia[c])
print(f'Os primeiros {n} números da sequência de fibonacci são :',sequencia)
