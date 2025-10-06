menu = """
Para começar, escolha uma das opções a seguir:
    [1] Extrato
    [2] Saque
    [3] Depósito
    [0] Sair
"""
menu2 = """
[1] Continuar
[0] Sair
"""

saldo = float(1500)
numero_saque_diario = 3

while True:
    opcao = int(input(menu))


    if opcao == 1:
        print(f"Seu saldo é de R$ {saldo:.2f} reais.")
        op2 = int(input(menu2))
        if op2 == 0:
            break


    elif opcao == 2:
        valor_saque = float(input(f"Digite o valor que você deseja sacar:  "))
        if (valor_saque <= saldo) and (valor_saque <= 500.00) and (numero_saque_diario > 0):
            saldo -= valor_saque
            numero_saque_diario -= 1
            print()
            print(f"Saque de R$ {valor_saque:.2f} reais efetuado com sucesso!")
        op2 = int(input(menu2))
        if op2 == 0:
            break

        elif (valor_saque > 500.00) and (valor_saque <= saldo):
            print()
            print("Não foi possível realizar a operação pois o limite de valor do saque é de R$ 500.00 reais")
            op2 = int(input(menu2))
            if op2 == 0:
                break

        elif numero_saque_diario == 0:
            print("Você atingiu o limite de saques diário, tente novamente em outro dia.]")
            op2 = int(input(menu2))
            if op2 == 0:
                break

            else:
                print()
                print("Falha na operação, saldo insuficiente.")
                op2 = int(input(menu2))
                if op2 == 0:
                    break



    elif opcao == 3:
        valor_deposito = float(input(f"Digite o valor que você deseja depositar:  "))
        saldo += valor_deposito
        print(f"Depósito de {valor_deposito:.2f} reais realizado com sucesso!")
        op2 = int(input(menu2))
        if op2 == 0:
            break

    elif opcao == 0:
        break


    else:
        break


print("Obrigado, até logo")
