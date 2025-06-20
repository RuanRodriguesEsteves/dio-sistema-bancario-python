from datetime import datetime

#Menus
menu = """
==================== MENU BANCÁRIO ====================

[1] 💸 Sacar
[2] 💰 Depositar
[3] 📄 Visualizar Extratos
[4] 💸 Visualizar Saldo
[0] 🚪 Sair

=======================================================
Digite a opção desejada: """

menu_extrato = """
==================== MENU DE EXTRATOS ====================

[1] 💸 Extrato de Saques
[2] 💰 Extrato de Depósitos
[3] 📄 Todos os Extratos
[0] 🚪 Voltar

==========================================================
Digite a opção desejada: """

#Fim Menus

#Variáveis Globais
saldo = 0
extrato = []
LIMITE_SAQUE = 3
#Fim Variáveis Globais

#Função para validar e formatar a entrada do usuário
def formatar_float(valor: str):
    valor = valor.replace(",", ".")
    try:
        valor = float(valor)
        
    except ValueError:
        raise ValueError("Digíte um valor numérico.")
    
    if valor > 0:
        return valor
    else:
        raise ValueError("O valor precisa ser maior que 0.")

#Função para armazenar o extrato dentro da variável global extrato
def armazenar_extrato(tipo, valor):
    transacao = {
        "data_hora": datetime.now(),
        "tipo": tipo,
        "valor": valor
    }
    extrato.append(transacao)

#Função para subtrair o valor passado pelo usuário da variável global saldo
def sacar(valor):
    armazenar_extrato("Saque", valor)
    return valor

#Função para acrescentar o valor passado pelo usuário da variável global saldo
def depositar(valor):
    armazenar_extrato("Depósito", valor)
    return valor

#Função para exibir o extrato conforme filtro passado pelo usuário
def visualizar_extrato(tipo, saldo):
    if verificar_quantidade_extrato("") > 0:
        for extrato_tipo in extrato:
            if (tipo == "Depósito" and verificar_quantidade_extrato("Depósito") > 0) or (tipo == "Saque" and verificar_quantidade_extrato("Saque") > 0):
                if extrato_tipo["tipo"] == tipo:
                    print(f"Data e Hora: {extrato_tipo['data_hora']}\nTipo: {extrato_tipo['tipo']}\nValor: R$ {extrato_tipo['valor']}\n\n\n")
            elif tipo == "Todos":
                print(f"Data e Hora: {extrato_tipo['data_hora']}\nTipo: {extrato_tipo['tipo']}\nValor: R$ {extrato_tipo['valor']}\n\n\n")
            else:
                print("Não foram realizadas movimentações para o tipo de transação selecionada.")
    else:
        print("Não foram realizadas movimentações.")
                
    print(f"\nSaldo Atual: R$ {saldo:.2f}")

def verificar_quantidade_extrato(tipo):
    if tipo == "Saque":
        quantidade = sum(
            1 for extrato_saque in extrato
            if extrato_saque["tipo"] == "Saque" and extrato_saque["data_hora"].date() == datetime.now().date()
        )
    else:
        quantidade = sum(1 for extrato_saque in extrato)

    return quantidade

while True:
    opcao = input(menu)

    if opcao == "1":
        quantidade_saque = verificar_quantidade_extrato("Saque")
        if quantidade_saque < 3:
            try:
                valor = formatar_float(input("Digite o Valor Do Saque:"))
                
                if saldo > valor and valor <= 500:
                    saldo -= sacar(valor)
                elif valor > 500:
                    print("Valor do saque maior que R$ 500,00")
                elif saldo < valor:
                    print("Valor do saque maior que saldo.")
                else:
                    print("Erro não identificado.")
                
            except ValueError as erro:
                    print(f"Erro: {erro}. Tente novamente!")
        else:
            print("Limite de saque diário atingida.")

    elif opcao == "2":
        try:
            saldo += depositar(formatar_float(input("Digite o Valor Do Depósito:")))
        except ValueError as erro:
            print(f"Erro: {erro}. Tente novamente!")

    elif opcao == "3":
        while True:
            opcao_menu = input(menu_extrato)

            if opcao_menu == "1":
                visualizar_extrato("Saque", saldo)
            
            elif opcao_menu == "2":
                visualizar_extrato("Depósito", saldo)
        
            elif opcao_menu == "3":
                visualizar_extrato("Todos", saldo)

            elif opcao_menu == "0":
                break

    elif opcao == "4":
        print(f"R$ {saldo}")

    elif opcao == "0":
        break
