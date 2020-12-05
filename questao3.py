#-*- coding: UTF-8 -*-
from random import randint

contar_1 = 0
contar_2 = 0
contar_3 = 0
contar_4 = 0
contar_5 = 0
contar_6 = 0

for i in range(20):
  numero_sorteado = (randint(1, 6))
  print(numero_sorteado, end = ',')
  if numero_sorteado == 1:
    contar_1 += 1
  elif numero_sorteado == 2:
    contar_2 += 1
  elif numero_sorteado == 3:
    contar_3 += 1
  elif numero_sorteado == 4:
    contar_4 += 1
  elif numero_sorteado == 5:
    contar_5 += 1
  else :
    contar_6 += 1

print('\b.\n')
print("***********************************")
print(f"* Numero 1 foi sorteado {contar_1} vez(es) * ")
print(f"* Numero 2 foi sorteado {contar_2} vez(es) * ")
print(f"* Numero 3 foi sorteado {contar_3} vez(es) * ")
print(f"* Numero 4 foi sorteado {contar_4} vez(es) * ")
print(f"* Numero 5 foi sorteado {contar_5} vez(es) * ")
print(f"* Numero 6 foi sorteado {contar_6} vez(es) * ")
print("***********************************")