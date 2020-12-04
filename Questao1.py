#-*- coding: UTF-8 -*-
print('****************')
print('* Questionario *')
print('****************')
todos_os_candidatos = list()
candidato = []
idade = int(input('Digite a idade: '))

while idade != 0:
    candidato.clear()
    sexo = input("Digite o sexo m/f: ")
    experiencia = input("Digite a experiencia s/n: ")
    candidato.append(idade)
    candidato.append(sexo.lower())
    candidato.append(experiencia.lower())
    idade = int(input("Digite a idade: "))
    todos_os_candidatos.append(candidato.copy())
print(todos_os_candidatos)

conta_sexo_m = 0
conta_sexo_f = 0
idade_masculina = []
conta_exp_m = 0
maior_de_45 = 0
menor_21_exp_f = []

for elemento in todos_os_candidatos:
    print(elemento)
    if elemento.__contains__('m'):
        conta_sexo_m += 1
        idade_masculina.append(elemento[0])
        if elemento[0] >= 45:
            maior_de_45 += 1
        if elemento.__contains__('s'):
            conta_exp_m += 1
    else:
        conta_sexo_f += 1
        if elemento.__contains__('s'):
            if elemento[0] <= 21:
                menor_21_exp_f.append(elemento[0])
    # conta_sexo_m += i.count('m')
    #conta_sexo_f += i.count('f')
print(f"O numero de candidados do sexo feminino é {conta_sexo_f}")
print(f"O numero de candidados do sexo masculino é {idade_masculina.a}")
print(f"O media da idade masculina é {conta_sexo_m}")
print(f"O porcentagem de homens maiores de 45:{maior_de_45}") #falta calcular porcentagem
print(f"com exp = {conta_exp_m}")