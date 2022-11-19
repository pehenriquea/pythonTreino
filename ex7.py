# Faça um Programa que pergunte quanto você
# ganha por hora e o número de horas trabalhadas
# no mês. Calcule e mostre o total do seu salário
# no referido mês.

print("Digite o valor da hora trabalhada: ")
horaT = float(input())
print("Digite a quantidade de horas trabalhadas nesse mês: ")
horasMes = float(input())
salario = horasMes * horaT
print("Seu salário é R$" + str(salario))
