#Desafio
#Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

#Entrada
#A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

#Saída
#Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.


N = int(input("Informe o número de testes que deseja realizar: "))  # lê a quantidade de casos de teste como um valor inteiro

while N > 0:
    A, B = input().split()  # lê os valores A e B como strings separados por um espaço
    if A.endswith(B):  # verifica se B é uma substring no final de A
        print("encaixa")  # imprime "encaixa" caso B seja uma substring no final de A
    else:
        print("nao encaixa")  # imprime "nao encaixa" caso contrário
    N -= 1  # decrementa N a cada iteração do loop
