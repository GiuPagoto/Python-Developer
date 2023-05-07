#EX1
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    print(numero)

#EX2
for numero in range(100):

    if numero == 10:
        break

    print(numero, end=" ")

#EX3
for numero in range(100):

    if numero == 10:
        continue #vai pular o 10

    print(numero, end=" ")

#EX4: exibir só os números pares dentro da sequência

#for numero in range(100):

    #if numero % 2 == 0:
        #continue #vai pular o 10

    #print(numero, end=" ")

#EX5
#while True:
    #numero = int(input("Informe um número: "))

    #if numero == 10:
        #break

    #if numero % 2 == 0:
        #continue

    #print(numero)