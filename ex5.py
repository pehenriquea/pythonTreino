#Faça um Programa que peça o raio de um círculo,
#calcule e mostre sua área.
import math

print("Digite um raio: ")
raio = float(input()) * 2 * math.pi
raio = round(raio, 2)
print("A area do círculo é "+ str((raio)))
