#-*- coding: UTF-8 -*-
valor = int(input('Insira um valor: '))
lista_valor = []

while valor >= 0:
  lista_valor.append(valor)
  valor = int(input('Insira um valor: '))

print(f"O maior numero é: {max(lista_valor)}")
print(f"O menor numero é: {min(lista_valor)}")