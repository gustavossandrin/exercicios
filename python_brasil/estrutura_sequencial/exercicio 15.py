"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
 total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo
"""
ganho_por_hora = int(input('quanto você ganha por hora trabalhada? '))
horas_trabalhadas_por_mes = int(input('quantas horas você trabalaha por mês? '))

# calculo dos descontos
salario_bruto = ganho_por_hora * horas_trabalhadas_por_mes
desconto_inss = salario_bruto * 0.08
desconto_imposto_de_renda = salario_bruto * 0.11
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - desconto_sindicato - desconto_inss - desconto_imposto_de_renda

# prints
print(f'+ Salário Bruto : {salario_bruto}R$')
print(f'- IR (11%) : {desconto_imposto_de_renda}R$')
print(f'- INSS (8%) : {desconto_inss}R$')
print(f'- Sindicato (5%) : {desconto_sindicato}R$')
print(f'= Salário Liquido : {salario_liquido}R$')
