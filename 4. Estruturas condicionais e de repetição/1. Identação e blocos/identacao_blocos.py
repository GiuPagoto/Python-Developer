#def sacar(valor: float) 
#método sacar, que recebe um valor que é float
#a marcação do float é opcionar.
#pode deixar assim: def sacar (valor):

def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    
    print("Obrigada por ser nosso cliente, tenha um bom dia!")

def depositar(valor):
    saldo = 500
    saldo += valor
    

sacar(600)

