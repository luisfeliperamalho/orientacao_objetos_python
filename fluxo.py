# função para criar o objeto conta
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular,
             "saldo": saldo, "limite": limite}
    return conta

# função adicionar valor ao saldo
def deposita(conta, valor):
    conta["saldo"] += valor
    
# função remove valor do saldo
def saca(conta, valor):
    conta["saldo"] -= valor

# função retorna valor do saldo
def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))
