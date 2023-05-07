texto = input("Informe um texto: ") 
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print() #adiciona uma quebra de linha





#texto informado: "python"
#for: vai percorrer letra por letra do texto informado
#letra.upper(): vai transformar as letras minúsculas em maiúsculas para verificar se a letra está dentro da sequência de vogais informada
#letra = p --> P 
#letra = y --> Y 
#letra = t --> T 
#letra = h --> H 
#letra = o --> O 
#letra = n --> N
#print(letra, end=""): informa quais letras do texto informado fazem parte da sequência de vogais