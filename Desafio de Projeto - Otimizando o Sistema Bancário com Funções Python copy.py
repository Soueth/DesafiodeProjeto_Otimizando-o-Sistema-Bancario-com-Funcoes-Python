extrato_saldo = [float(), float(), float()]
saldo = float()
numero_saques = int()
limite_saques= 3
Acesso = 0
usuario = int()
menu = """Escolha uma opção:
    1 - Depositar
    2 - Sacar
    3 - Visualizar extrato
    0 - Sair/Finalizar
"""  
usuarios = {}
contador_contas = int()
conta = {"Número da conta": contador_contas, "Agência": "0001"}
contas = {usuario: {}}

def fazer_cadastro():
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
        print(usuarios)
    
    else:
        print("Você já está cadastrado!!!")

def criar_conta():
    global contador_contas
    contador_contas += 1
    conta["Número da conta"] = contador_contas
    contas[usuario] = conta

def autenticar():
    global Acesso
    usuario = int(input("Insira o seu CPF (Apenas os números) "))
    senha = int(input("insira uma senha "))
    true_key = int(usuarios.get(usuario, {}).get("Senha"))
 
    if true_key == senha:
        Acesso = 1
 
    else:
        print("Usuário ou Senha Incorreta!!\n")

def deposito(valor,extrato,/):
    global saldo
 
    if valor <= 0:
        print("Não se pode depositar valores iguais ou menores do que zero")
 
    else:
        saldo += valor
        extrato += valor
        return float(extrato)
    
def saque(*,valor, limite):
    global saldo, numero_saques, limite_saques

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

def vizualizar_extrato(saldo,/,*,extrato):
    for cont_saldos in range(0,3,1):
        print("saldo -",cont_saldos+1,":",extrato_saldo[cont_saldos],"\n")
    print(f"O extrato do(s) depósito(s) é de: {extrato}\n")
    print(f"O seu saldo atual é de {float(saldo):.2f}\n")

opcao_cadastro = int(input("""
    Bem-vindo(a) ao nosso banco!!!
    
    |Digite - 1| = Se já tem um cadastro e deseja fazer login.
    |Digite - 2| = Se ainda não tem um e gostaria de fazer o cadastro.
    |Digite - 0| = Se gostaria de sair.
"""))

if opcao_cadastro == 1:
    autenticar()

elif opcao_cadastro == 2:
    fazer_cadastro()
    print(usuarios)

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
                extrato_deposito = deposito(valor, extrato_deposito)

            elif opcao == 2:
                while True:
                    valor = float(input("Qual o valor a sar sacado?\n"))
                    saque(valor=valor,limite=500)
                    print(f"Seu saldo é de R$ {float(saldo):.2f}")

                    if numero_saques >= limite_saques:
                        break
                    
                    print("Gostaria de fazer outro saque?\n")
                    print("     | 0 - NÃO |\n")
                    outro_saque = input("     | 1 - SIM |\n")

                    if outro_saque == 0:
                        break

            elif opcao == 3:
                print("===========EXTRATO===========\n")
                vizualizar_extrato(saldo, extrato = extrato_deposito)

            else:
                break 

    elif opcao_operacao == 2:
        criar_conta()
        print("Conta criada!!!")

print("Obrigado por usar nosso serviço!!!")