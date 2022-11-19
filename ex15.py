# Faça um Programa para uma loja de tintas. O programa
# deverá pedir o tamanho em metros quadrados da área a
# ser pintada. Considere que a cobertura da tinta é de
# 1 litro para cada 6 metros quadrados e que a tinta é
# vendida em latas de 18 litros, que custam R$ 80,00 ou
# em galões de 3,6 litros, que custam R$ 25,00. Informe
# ao usuário as quantidades de tinta a serem compradas
# e os respectivos preços em 3 situações:
# a - comprar apenas latas de 18 litros;
# b - comprar apenas galões de 3,6 litros;
import math

print("Digite a área a ser pintada (em metro/quadrado): ")
metroQ = float(input())

litro = metroQ * 6
latas = litro / 18
valorLata = latas * 80
galao = litro / 3.6
valorGalao = galao * 25
print("Quantidade de latas a serem compradas: " + str(math.ceil(latas)))
print("Valor: R$" + str(math.ceil(valorLata)))
print("Quantidade de galões a serem compradas: " + str(math.ceil(galao)))
print("Valor: R$" + str(math.ceil(valorGalao)))
