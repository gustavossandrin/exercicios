"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
 Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
 (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
 variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
  e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""


def mostrar_kg_de_peixe_em_excesso(kg_de_peixe):
    kg_a_mais = kg_de_peixe - 50
    if kg_a_mais <= 0:
        return 'nenhum peso a mais'
    else:
        return f'voce excedeu em {kg_a_mais}kg, o valor da multa sera: {kg_a_mais * 4}'


if __name__ == '__main__':
    print(mostrar_kg_de_peixe_em_excesso(23))
