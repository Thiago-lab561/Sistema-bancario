
menu="""
    Menu Bancario
    ==========================
    [0]-Saque
    [1]-Saldo
    [2]-Extrato
    [5]-Depósito
    [4]-Sair
    ==========================
    
    Insira a operação necessária
"""
print(menu)

Saldo=1500
LIMITE_SAQUE=3
numero_saque=0
extrato=''

while True:
    
    resposta=input('Insira a operação desejada:')
    if int(resposta)==0:
        if Saldo<1:
            print('Saldo insufisciente')
        else:
            valor=float(input('Insira o valor para saque: '))
            Saldo_conta=Saldo-valor
            if float(valor)>float(Saldo):
                print('Valor indisponivel para saque!')
                
            elif numero_saque>=LIMITE_SAQUE:
                print('Limite excedido')
                break
            else:
                calculo=Saldo_conta
                reais=float(calculo)
                print(f'Saldo atual: R$ {reais:.2f}')
                print(f'Valor sacado de: R$ {valor:.2f}')
            
            if valor>0:
                numero_saque+=1
                Saldo=Saldo_conta
                extrato+=f'{valor:.2f}\n'
    
    elif int(resposta)==1:
        print(f'R$ {Saldo:.2f}')
    
    
    elif int(resposta)==2:
        print("\n===========EXTRATO DE CONTA===========")
        print("\nNão foram realizadas movimentações nesta conta" if not extrato else extrato)
        print("\n======================================")
    
    elif int(resposta)==5:
        deposito=float(input('Insira o valor a ser depositado'))
        valor_atual=Saldo+deposito
        print("\n============Depositado com sucesso============")
        print(f'\nSaldo atual: R${valor_atual:.2f}')
        print("\n========================")

    elif int(resposta)==4:
        break

    else:
        print("Operação invalida!")
        break