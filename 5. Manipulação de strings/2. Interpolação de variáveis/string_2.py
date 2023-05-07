nome = "Giullia"
idade = 24
profissao = "Estudante"
linguagem = "Python"
saldo = 45.435

#dicionário
dados = {"nome": "Giullia", "idade": 24}

#Old style %
print("Nome: %s Idade: %d" % (nome, idade))

#Método format {}
print("Nome: {} Idade: {}".format(nome, idade))

#Método format {1} {0}
print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

#Método format {nome} {idade}
print("Nome: {nome} Idade: {idade}".format(nome = nome, idade = idade))

print("Nome: {name} Idade: {age} {name} {name} {age}".format(name = nome, age = idade))

#Método format com dicionário
print("Nome: {nome} Idade: {idade}".format(**dados))

#Método f-string
print(f"Nome: {nome} Idade: {idade}")

#Método f-string com formatação
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")

print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")


