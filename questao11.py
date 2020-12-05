#-*- coding: UTF-8 -*-
divisivel_4 = []
for i in range(0,200):
  if i % 4 == 0:
    divisivel_4.append(i)
print(f"Os numeros menores que 200 divisíveis por 4 são:{divisivel_4}")