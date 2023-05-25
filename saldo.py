saldo = 0

def mostrar_saldo():
    print("Seu saldo é:", saldo)

def efetuar_deposito():
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        global saldo
        saldo += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")

def efetuar_saque():
    valor = float(input("Digite o valor do saque: "))
    if valor > 0 and valor <= saldo:
        global saldo
        saldo -= valor
        print("Saque realizado com sucesso.")
    else:
        print("Saldo insuficiente ou valor inválido.")

while True:
    print("----- Menu -----")
    print("1 - Mostrar Saldo")
    print("2 - Efetuar Depósito")
    print("3 - Efetuar Saque")
    print("4 - Finalizar Sessão")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_saldo()
    elif opcao == "2":
        efetuar_deposito()
    elif opcao == "3":
        efetuar_saque()
    elif opcao == "4":
        print("Sessão finalizada.")
        break
    else:
        print("Opção inválida. Tente novamente.")
