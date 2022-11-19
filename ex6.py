# Faça um Programa que calcule a área
# de um quadrado, em seguida mostre o dobro
# desta área para o usuário.
import math

print("Digite um lado do quadrado: ")
lado = float(input())
lado = math.pow(2, lado)*2
print("O dobro da área do quadrado é "+ str((lado)))
