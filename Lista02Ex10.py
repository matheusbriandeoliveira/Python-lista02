'''
Calcule as raízes da equação de 2o grau.
'''
from math import sqrt

print('Informe os coeficientes de uma equação de 2º grau')
a = float(input('a >> '))
if a == 0:
    print('Não é equação de 2º grau')
else:
    b = float(input('b >> '))
    c = float(input('c >> '))
    delta = b*b - 4*a*c
    if delta < 0:
        print('Não existe raiz real')
    else:
        x1 = (-b + sqrt(delta)) / (2*a)
        x2 = (-b - sqrt(delta)) / (2*a)
        if delta == 0:
            print(f'Existe uma raiz >> x = {x1}')
        else:
            print(f'Existem 2 raízes >> x1 = {x1} e x2 = {x2}')
