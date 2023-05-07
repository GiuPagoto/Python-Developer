nome = "gIuLlIa"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto  + ".")
print(texto.strip() + ".") #elimina os espaços
print(texto.lstrip() + ".") #elimina os espaços da esquerda
print(texto.rstrip() + ".") #elimina os espaços da direita

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))

#ex: iteração

for letra in menu:
    print(letra, end="-")
print()