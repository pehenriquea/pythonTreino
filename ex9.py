# Faça um Programa que peça a temperatura em
# graus Celsius, transforme e mostre em
# graus Fahrenheit.

print("Digite os graus celsius: ")
tempC = float(input())
tempF = tempC * 1.8 + 32
tempF = round(tempF, 2)
print("Temperatura em celsius: " + str(tempF))
