# -*- coding: UTF-8 -*-
print("**********************")
print(" Calcula conta de luz ")
print("**********************\n")

consumidor = []
consumidores = []
gasto_quilowatts = 1

while gasto_quilowatts != 0:
    consumidor.clear()
    tipo_consumo = int(input("Escolha o tipo de consumo: (1)residencial, (2)comercial, (3)industrial:  \n"))
    if tipo_consumo == 0:
        break
    consumidor.append(tipo_consumo)
    salario_minimo = float(input("Digite o valor do salário mínimo: "))
    consumidor.append(salario_minimo)
    gasto_quilowatts = float(input("Digite a quantidade consumida em quilowatts ou (0) para sair: "))
    consumidor.append(gasto_quilowatts)
    consumidores.append(consumidor.copy())

valor_kw = []
calculo_acresc = []

for cliente in consumidores:
    valor_kw.append(cliente[1] / 8)
    if cliente[0] == 1:
        calculo_base = (cliente[1] / 8) * cliente[2]
        acrescimo = calculo_base * 0.05
        calculo_acresc.append(calculo_base + acrescimo)
    if cliente[0] == 2:
        calculo_base = (cliente[1] / 8) * cliente[2]
        acrescimo = calculo_base * 0.1
        calculo_acresc.append(calculo_base + acrescimo)
    if cliente[0] == 3:
        calculo_base = (cliente[1] / 8) * cliente[2]
        acrescimo = calculo_base * 0.15
        calculo_acresc.append(calculo_base + acrescimo)

print("\n*********************************************************")
for k, v in enumerate(valor_kw):
    print(f"O valor em kw do cliente {k + 1} é igual a {v}")
print("*********************************************************\n")

print("*********************************************************")
for k, v in enumerate(calculo_acresc):
    print(f"O valor a ser pago pelo consumidor {k + 1} é igual a {round(v, 2)}")
print("*********************************************************\n")

print("*********************************************************")
print(f"O faturamento da empresa de energia é de: {sum(calculo_acresc)}")
print("*********************************************************\n")
contar_consumidor = 0
for valor in calculo_acresc:
    if 500 <= valor < 1000:
        contar_consumidor += 1

print("*********************************************************")
print(f"A quantidade de consumidores que pagam entre R$ 500 e \nR$1000 é de: {contar_consumidor}")
print("*********************************************************\n")