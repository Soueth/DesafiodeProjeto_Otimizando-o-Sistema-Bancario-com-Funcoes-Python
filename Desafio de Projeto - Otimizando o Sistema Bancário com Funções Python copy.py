def main():
    extrato_saldo = [float(), float(), float()]
    saldo = float()
    numero_saques = int()
    limite_saques= 3
    Acesso = int()
    usuario = int()
    menu = """Escolha uma opção:
        1 - Depositar
        2 - Sacar
        3 - Visualizar extrato
        0 - Sair/Finalizar
    """  
    limite = 500
    usuarios = {}
    
    while True:
        opcao_cadastro = int(input("""
        Bem-vindo(a) ao nosso banco!!!
        
        |Digite - 1| = Se já tem um cadastro e deseja fazer login.
        |Digite - 2| = Se ainda não tem um e gostaria de fazer o cadastro.
        |Digite - 0| = Se gostaria de sair.
        """))

        if opcao_cadastro == 1:
            Acesso = autenticar(usuarios)

        elif opcao_cadastro == 2:
            fazer_cadastro(usuarios, usuario)
            print(usuarios)

        if (opcao_cadastro == 0) or (Acesso == 1):
            break
            
    Acesso = 1
    if Acesso == 1:
        opcao_operacao = int(input("""
        |Digite - 1| = Se gostaria de fazer uma operação
        |Digite - 2| = Se gostaria de criar uma nova conta
        |Digite - 0| = Se gostaria de sair.
                                
    """))

        if opcao_operacao == 1:
            while True:
                opcao = int(input(menu))

                if opcao == 1:
                    valor = float(input("Qual o valor a ser depositado?\n"))
                    extrato_deposito = float()
                    extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

                elif opcao == 2:
                    while True:
                        valor = float(input("Qual o valor a sar sacado?\n"))
                        saldo, numero_saques =saque(valor=valor, limite=limite, extrato_saldo=extrato_saldo, saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques)
                        print(f"Seu saldo é de R$ {float(saldo):.2f}")

                        if numero_saques >= limite_saques:
                            break
                        
                        print("Gostaria de fazer outro saque?\n")
                        print("     | 0 - NÃO |\n")
                        outro_saque = int(input("     | 1 - SIM |\n"))

                        if outro_saque == 0:
                            break

                elif opcao == 3:
                    print("===========EXTRATO===========\n")
                    vizualizar_extrato(saldo, numero_saques, extrato_deposito = extrato_deposito, extrato_saldo = extrato_saldo)

                else:
                    break 

        elif opcao_operacao == 2:
            criar_conta(usuario)
            print("Conta criada!!!")

    print("Obrigado por usar nosso serviço!!!")

def fazer_cadastro(usuarios, usuario):
    CPF = int(input("Qual o seu CPF (Apenas os números)?\n"))
    if CPF not in usuarios:  
        valores = {}
        
        name = input("Informe seu nome completo\n")
        valores["Nome"] = name
        
        dia_do_nasc = str(input("O dia do seu nascimento:  "))
        mes_do_nasc = str(input("O mês:  "))
        ano_do_nasc = str(input("Do ano:  "))
        data_de_nasc = dia_do_nasc+"/"+mes_do_nasc+"/"+ano_do_nasc
        valores["Data de Nascimento"] = data_de_nasc
        
        print("Nos informe seu endereço para concluir o cadastro")
        logradouro = str(input("O logradouro:  "))
        numero_residencia = str(input("O nº da residência:  "))
        bairro = str(input("O bairro:  "))
        cidade = str(input("A cidade:  "))
        sigla_estado = str(input("A sigla do Estado:  "))
        endereco = logradouro+", "+numero_residencia+" - "+bairro+" - "+cidade+"/"+sigla_estado
        valores["Endereço"] = endereco
        
        print("Cadastrado!!!")
      
        senha = input("Crie uma senha:\n")
        valores["Senha"] = senha
        usuario = {}
        usuario[CPF] = valores
        usuarios.update(usuario)
    
    else:
        print("Você já está cadastrado!!!")

    return CPF

def criar_conta(usuario):
    contador_contas = int()
    conta = {"Número da conta": contador_contas, "Agência": "0001"}
    contador_contas += 1
    conta["Número da conta"] = contador_contas
    contas = {usuario: {}}
    contas[usuario] = conta

def autenticar(usuarios):
    Acesso_concedido = 0
    username = int(input("Insira o seu CPF (Apenas os números) "))
    senha = int(input("insira uma senha "))
    
    if username in usuarios:
        true_key = int(usuarios.get(username).get("Senha"))
        print(true_key)

        if true_key == senha:
            Acesso_concedido = 1

        else:
            print("Senha Incorreta!!\n")

    else: 
        print("Usuário Incorreto ou não existe!!")

    return Acesso_concedido

def deposito(saldo, valor, extrato,/):
    if valor <= 0:
        print("Não se pode depositar valores iguais ou menores do que zero")
 
    else:
        saldo += valor
        extrato += valor
        return extrato, saldo
    
def saque(*,saldo, numero_saques, limite_saques, valor, limite, extrato_saldo):

    if valor > saldo:
        print("O valor a ser sacado não pode ser maior do que o saldo!!!\n")
        print(f"SALDO: {float(saldo):.2f}\n")
    

    elif valor > limite:
        print(f"O valor não pode ser sacado, O limite é de R${float(limite):.2f}\n")
    
    elif valor <= 0:
        print("Valores iguais a zero ou negativos não podem ser sacados!!!\n")

    elif numero_saques < limite_saques:               
        saldo -= valor
        print(f"Valor sacado!!!\n")
        extrato_saldo[numero_saques] = f"{float(valor):.2f}"
        numero_saques += 1

    else:
        print(f"Apenas é permitido sacar {limite_saques} vezes por dia!!!\n")

    return saldo, numero_saques  

def vizualizar_extrato(saldo,numero_saques,/,*,extrato_deposito, extrato_saldo):
    for cont_saldos in range(0,numero_saques,1):
        print("saque -",cont_saldos+1,":",extrato_saldo[cont_saldos],"\n")
    print(f"O extrato do(s) depósito(s) é de: {extrato_deposito}\n")
    print(f"O seu saldo atual é de {float(saldo):.2f}\n")

main()