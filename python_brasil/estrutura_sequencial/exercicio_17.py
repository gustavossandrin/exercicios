"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
*comprar apenas latas de 18 litros;
*comprar apenas galões de 3,6 litros;
*misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.
"""
# preços das latas:
import math
from math import ceil

preco_latas_de_18_litros = 80
preco_galao_de_3_litros = 25
# calculando a tinta necessaria
area_a_ser_pintada = int(input('qual a area em m2 a ser pintada? '))
tinta_necessaria = area_a_ser_pintada / 6
# preço de comprar só latas de 18
latas_de_18_necessarias = ceil(tinta_necessaria / 18)
print(f'se você comprar somente latas de 18 litros, vai precisar de {latas_de_18_necessarias} latas e o preço sera de {latas_de_18_necessarias * 80}')
# preço de comprar só galoes de 3.6 litros
galoes_de_3_necessarios = ceil(tinta_necessaria / 3.6)
print(f'se voce comprar somente galoes de 3.6 litros, ira precisar de {galoes_de_3_necessarios} galoes e o preço vai ser {galoes_de_3_necessarios * 25}')
# preço de misturar latas e galoes
latas_de_18_necessarias = math.floor(tinta_necessaria / 18)
tinta_restante = tinta_necessaria % 18
galoes_de_3_necessarios = math.ceil(tinta_restante / 3.6)
valor_galoes = galoes_de_3_necessarios * 25
valor_latas = latas_de_18_necessarias * 80
valor_total = valor_latas + valor_galoes
print(f'voce vai precisar comprar {latas_de_18_necessarias} latas e mais {galoes_de_3_necessarios} galoes, no valor de {valor_total}')