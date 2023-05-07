#DESAFIO
#O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.

#Entrada
#A entrada é uma linha de texto T (1 ≤ |T| ≤ 500).

#Saída
#A saída é dada em uma única linha. Ela deve ser "TWEET" (sem as aspas) se a linha de texto T tem até 140 caracteres. Se T tem mais de 140 caracteres, a saída deve ser "MUTE".

#Exemplo de Entrada
#RT @TheEllenShow: If only Bradley's arm was longer. Best photo ever. #oscars pic.twitter.com/C9U5NOtGap

#Exemplo de Saída
#TWEET

#CÓDIGO

#lê a entrada de texto
T = input("Digite o seu tweet: ") 

# verifica o comprimento do texto
caracter = len(T)


if caracter <= 140:
  print("TWEET")
else:
  print("MUTE")