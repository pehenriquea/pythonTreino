# Faça um Programa que peça a temperatura em graus
# Fahrenheit, transforme e mostre a temperatura
# em graus Celsius.

print("Digite os graus fahrenheit: ")
tempF = float(input())
tempC = 5 * ((tempF-32)/9)
tempC = round(tempC, 2)
print("Temperatura em celsius: " + str(tempC))
