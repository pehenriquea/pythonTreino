# Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58

print("Digite a altura: ")
altura = float(input())
peso = (72.7 * altura) - 58
peso = round(peso, 2)
print(str(peso))
