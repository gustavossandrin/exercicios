"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
 Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
from math import ceil

area_a_ser_pintada = int(input('qual a area em metros quadrados a ser pintado? '))
quantidade_de_tinta = area_a_ser_pintada / 3
quantidade_galoes = ceil(quantidade_de_tinta / 18)
preco_dos_galoes = quantidade_galoes * 80
print(f'latas a serem compradas: {quantidade_galoes}')
print(f'preço a ser pago: {preco_dos_galoes}')