menu = """

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Informe o valor do depósito:"))
        
        if valor > 0:
            saldo += valor
            extrato += f" Depósito: R${valor:.2f}\n"
            print("Depósito efetuado com sucesso!")
        
        else:
            print("Operação falhou! Valor informado inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque:"))

        excedeu_max_saques = numero_de_saques >= LIMITE_SAQUES
        
        excedeu_limite = valor > limite
        
        excedeu_saldo = valor > saldo

        if excedeu_max_saques:
            print("Operação falhou! Excedeu o limite de saques")

        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede limite!")

        elif excedeu_saldo:
            print("Operação falhou! Excedeu seu saldo!")            
        
        elif valor > 0:
            saldo -= valor
            extrato += f" Saque: R${valor:.2f}\n"
            numero_de_saques += 1
            print("Saque efetuado com sucesso!")
        
        else:
            print("Operação falhou! Valor excedeu o saldo.")
    
    elif opcao == "e":
        print("\n##### EXTRATO #####")
        print("Sem operações." if not extrato else extrato)
        print(f"\nSaldo = R${saldo:.2f}")
        print("###################")

    elif opcao == "q":
        break
    else:
        print("Opção inválida")