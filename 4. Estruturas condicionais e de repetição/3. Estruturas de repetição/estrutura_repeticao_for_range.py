#início(inclusivo)
#fim(exclusivo)
#ex: 0 a 10 (inclui 0 e exclui 10, gera de 0 a 9)

#range(stop) -> range object
#range(start, stop[, step]) -> range object

#range(4)
#exibe: range(0,4)

#forçar exibição dos números: list(range(4))
#exibe: [0,1,2,3]

#UTILIZANDO RANGE COM FOR

#EX1:
# for numero in range(0,11):
    #print(numero, end="")
# >>> 0 1 2 3 4 5 6 7 8 9 10

#EX2: tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=" ")

#início = 0
#fim = 50
#step = 5
