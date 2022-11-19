# Faça um programa que peça o tamanho de um
# arquivo para download (em MB) e a velocidade
# de um link de Internet (em Mbps), calcule e
# informe o tempo aproximado de download do
# arquivo usando este link (em minutos).

print("Digite o tamanho do arquivo (em MB): ")
arq = float(input())
print("Digite a velocidade de banda (em Mbps): ")
banda = float(input())

mb = arq * 8
tempo = mb / banda

print("O download do arquivo será feito em " + str(round(tempo, 2)) + " segundos")
