"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo
que calcule seu peso ideal, usando a
seguinte fórmula: (72.7*altura) - 58
"""
def mostrar_peso_ideal(altura): # altura dever ser passada assim: 1.56
    peso_ideal = round((72.7 * altura) - 58)
    return peso_ideal


if __name__ == '__main__':
    print(mostrar_peso_ideal(1.80))
    print(mostrar_peso_ideal(1.68))
