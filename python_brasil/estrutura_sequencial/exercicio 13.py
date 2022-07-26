"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""


def mostrar_peso_ideal_por_genero(altura, sexo):
    if sexo == 'feminino':
        return round((62.1 * altura) - 44.7)
    else:
        return round((72.7 * altura) - 58)


if __name__ == '__main__':
    print(mostrar_peso_ideal_por_genero(1.67, 'feminino'))
    print(mostrar_peso_ideal_por_genero(1.86, 'masculino'))
