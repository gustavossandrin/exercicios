"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
1. o produto do dobro do primeiro com metade do segundo .
2. a soma do triplo do primeiro com o terceiro.
3. o terceiro elevado ao cubo.
"""
numero = int(input('digite um numero inteiro: '))
numero2 = int(input('digite outro numero inteiro: '))
numero3 = int(input('digite um numero real: '))

print(f'o produto do dobro do primeiro com metade do segundo = {(2 * numero) * (numero2 / 2)}')
print(f'a soma do triplo do primeiro com o terceiro = {(3 * numero) + numero3}')
print(f'o terceiro elevado ao cubo = {numero3 ** 3}')