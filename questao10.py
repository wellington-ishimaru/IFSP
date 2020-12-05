# -*- coding: UTF-8 -*-

numeros_impares = []
for i in range(0, 2001):
    if i % 2 != 0:
        numeros_impares.append(i)

print(f"Os números ímpares entre 0 e 2000 são: {numeros_impares}")
