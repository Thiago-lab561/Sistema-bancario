
clientes={'Cliente':'João','CPF':'222','Data de nascimento':'05/06/1920','Endereço':'Rua de são paulo,220','Agencia':'0001'}

def login():
    cliente=input('Insira seu nome: ')
    cpf=str(input('Insira seu CPF: '))
    if cliente not in clientes['Cliente'] or cpf not in clientes['CPF']:
        tela_login="""\n=================Tela de cadastro===============
            \nOlá usuario, verificamos em nosso sistema que você não possui cadastro.
            \nPedimos que preencha os dados abaixo para acessar o sistema
            \n==========================================================="""
        print(tela_login)
        cliente_cadastro=input('Insira seu primeiro nome: ')
        cpf_cadastro=input('Insira seu CPF: ').replace('.','')
        endereço_cadastro=input('Insira seu endereço: ')
        nascimento_cadastro=input('Insira sua data de nascimento: ')
        if cpf_cadastro in clientes['CPF']:
            print('CPF já registrado no sistema.')
            login()
        else:
            clientes['Cliente']=cliente_cadastro
            clientes['CPF']=cpf_cadastro
            clientes['Data de nascimento']=nascimento_cadastro
            clientes['Endereço']=endereço_cadastro
            agencia=int(clientes['Agencia'])+1
            clientes['Agencia']=f'{agencia:04}'
            

            print(clientes)
            print(f'\nSeja bem vindo,{cliente_cadastro}!')
            logado()
    else:
        print(f'\nBem vindo de volta,{cliente}!')
        logado()

def logado():
    Saldo=1500
    LIMITE_SAQUE=3
    numero_saque=0
    extrato=''
    while True:
        menu="""
    Menu Bancario
    ==========================
    [0]-Saque
    [1]-Saldo
    [2]-Extrato
    [5]-Depósito
    [4]-Sair
    ==========================
    
"""
        print(menu)
        
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
            deposito=float(input('Insira o valor a ser depositado: R$ '))
            valor_atual=Saldo+deposito
            print("\n============Depositado com sucesso============")
            print(f'\nSaldo atual: R${valor_atual:.2f}')
            print("\n========================")

        elif int(resposta)==4:
            break

        else:
            print("Operação invalida!")
            break
login()