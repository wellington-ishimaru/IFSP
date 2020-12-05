#-*- coding: UTF-8 -*-

conta_par = 0
soma = 0

for i in range(50,71):
  if i % 2 == 0:
    conta_par += 1
    soma += i

print(f"A soma dos pares entre 50 e 70 é: {soma}")
print(f"E a média é: {soma / conta_par}")