print("**************")
print("*Questionário*")
print("**************")
todos_os_candidatos = list()
candidato = []
idade = int(input("Digite a idade: "))
while idade != 0:
    candidato.clear()
    sexo = input("Digite o sexo m/f: ")
    experiencia = input("Digite a experiência s/n : ")
    candidato.append(idade)
    candidato.append(sexo)
    candidato.append(experiencia)
    idade = int(input("Digite a idade: "))
    todos_os_candidatos.append(candidato.copy())

print(todos_os_candidatos)
indice1 = 0
indice2 = 0
for candidato in todos_os_candidatos:
    soma_idade =+ todos_os_candidatos[candidato[i] for row in todos_os_candidatos][0]

print(soma_idade)