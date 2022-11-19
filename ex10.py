# Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# a - o produto do dobro do primeiro com metade do segundo .
# b - a soma do triplo do primeiro com o terceiro.
# c - o terceiro elevado ao cubo.

print("Digite o primeiro número inteiro: ")
num1 = int(input())
print("Digite o segundo número inteiro: ")
num2 = int(input())
print("Digite o terceiro número real: ")
num3 = float(input())

print("A: " + str((num1*2) * (num2/2)))
print("B: " + str((num1*3) + num3))
print("C: " + str(num3*num3*num3))
