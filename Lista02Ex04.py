'''
Sejam três números inteiros diferentes digitados pelo usuário, faça um programa que os coloque em ordem crescente.
'''
print('Informe 3 valores')
a = int(input('1º >> '))
b = int(input('2º >> '))
c = int(input('3º >> '))
'''
#Monstrando em ordem crescente
if a < b < c:
    print(f'Números em ordem crescente: {a} {b} {c}')
elif a < c < b:
    print(f'Números em ordem crescente: {a} {c} {b}')
elif b < a < c:
    print(f'Números em ordem crescente: {b} {a} {c}')
elif b < c < a:
    print(f'Números em ordem crescente: {b} {c} {a}')
elif c < a < b:
    print(f'Números em ordem crescente: {c} {a} {b}')
else:
    print(f'Números em ordem crescente: {c} {b} {a}')
'''
#Colocando em ordem crescente, por troca
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(f'Números em ordem crescente: {a} {b} {c}')
