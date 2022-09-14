'''
Uma receita para produzir um bolo conta com 2 xicaras de farinha de trigo, 3 ovos e 5 colheres de leite
(estes dados são constantes nesta receita). Você deve escrever um programa em Python que dados
como entrada A (quantidade de xicaras de farinha de trigo), B (quantidade de ovos) e C (quantidade
de colheres de leite) todos valores inteiros, o programa deve mostrar quantos bolos podem ser
produzidos.
'''
print('Informe a quantidade de ingredientes que possui')
A = int(input('Xícaras de farinha de trigo >> '))
B = int(input('Ovos >> '))
C = int(input('Colheres de leite >> '))
A = A // 2
B = B // 3
C = C // 5
if A < B and A < C:
    print(f'Conseguirá fazer {A} bolo(s)')
elif B < C:
    print(f'Conseguirá fazer {B} bolo(s)')
else:
    print(f'Conseguirá fazer {C} bolo(s)')
