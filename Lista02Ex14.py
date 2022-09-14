'''
Jogo da Roleta
'''
from random import randint

print('JOGO DA ROLETA')
numAp = int(input('Informe um número entre 1 e 36 para a aposta >> '))
valAp = float(input('Informe o valor da aposta >> R$ '))
numSt = randint(1,36)
print(f'O número sorteado foi {numSt}')
if numSt == numAp:
    print(f'Você ganhou 5 vezes o valor apostado = R$ {5 * valAp:.2f}')
elif (numSt-1) // 12 == (numAp-1) // 12:
    print(f'Você ganhou 3 vezes o valor apostado = R$ {3 * valAp:.2f}')
elif numSt % 2 == numAp % 2:
    print(f'Você ganhou 2 vezes o valor apostado = R$ {2 * valAp:.2f}')
else:
    print('Você perdeu o valor apostado!!')