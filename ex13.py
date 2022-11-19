# Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que
# são descontados 11% para o Imposto de Renda, 8% para o
# INSS e 5% para o sindicato, faça um programa que nos dê:
# a - salário bruto.
# b - quanto pagou ao INSS.
# c - quanto pagou ao sindicato.
# d - o salário líquido.

print("Digite o valor da hora trabalhada: ")
horaT = float(input())
print("Digite a quantidade de horas trabalhadas nesse mês: ")
horasMes = float(input())

salario = horasMes * horaT
ir = round(salario * 0.11, 2)
inss = round(salario * 0.08, 2)
sindicato = round(salario * 0.05, 2)
descontos = round(ir + inss + sindicato, 2)
salarioL = round(salario - descontos, 2)

print("+ Salario Bruto : R$" + str(salario))
print("- IR : R$" + str(ir))
print("- INSS : R$" + str(inss))
print("- Sindicato : R$" + str(sindicato))
print("= Salario Líquido : R$" + str(salarioL))
