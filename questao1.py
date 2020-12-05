#-*- coding: UTF-8 -*-

print("**************")
print(" Questionário ")
print("**************")
todos_os_candidatos = list()
candidato = []
idade = int(input("Digite a idade: "))

while idade != 0:
    candidato.clear()
    sexo = input("Digite o sexo m/f: ")
    experiencia = input("Digite a experiência s/n : ")
    candidato.append(idade)
    candidato.append(sexo.upper())
    candidato.append(experiencia.upper())
    idade = int(input("Digite a idade: "))
    todos_os_candidatos.append(candidato.copy())


conta_sexo_m = 0
conta_sexo_f = 0
idade_masculina = []
conta_exp_m = []
maior_de_45 = 0
menor_21_exp_f = 0
conta_exp_f = []
for elemento in todos_os_candidatos:
    if elemento.__contains__('M'):
        conta_sexo_m += 1
        idade_masculina.append(elemento[0])
        if elemento[0] >= 45:
            maior_de_45 += 1
        if elemento.__contains__('S'):
            conta_exp_m.append(elemento[0])
    else:
        conta_sexo_f += 1
        if elemento.__contains__('S'):
            conta_exp_f.append(elemento[0])
            if elemento[0] <= 21:
                menor_21_exp_f += 1
media_M_exp = 0
porcentagem_M_45 = 0
menor_F_exp = 0

# trata alguns erros caso não exista algum candidato de um determinado sexo
try:
    media_M_exp = sum(conta_exp_m)/len(conta_exp_m)
except ZeroDivisionError:
    pass
try:
    porcentagem_M_45 = round((maior_de_45 * 100) / conta_sexo_m, 2)
except ZeroDivisionError:
    pass
try:
    menor_F_exp = min(conta_exp_f)
except ValueError:
    pass

print("\n*****************************************************************")
print(f"O número de candidatos do sexo feminino é {conta_sexo_f}")
print(f"O número de candidatos do sexo masculino é {conta_sexo_m}")
print(f"O média da idade masculina com experiência é {media_M_exp}")
print(f"O porcentagem de homens maiores de 45 é {porcentagem_M_45}")
print(f"O número de mulheres com menos de 21 anos e com experiência é {menor_21_exp_f}")
print(f"A menor idade entre as mulheres com experiência é {menor_F_exp}")
print("****************************************************************")





