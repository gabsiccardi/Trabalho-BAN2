import psycopg2
from tabulate import tabulate
import datetime

def menu():
    print("Escolha a opção desejada:")
    print("1 - Exibir")
    print("2 - Adicionar")
    print("3 - Remover")
    print("4 - Editar")
    print("5 - Relatórios")
    print("0 - Sair")

def menuExibir():
    print("Escolha uma tabela")
    print("1 - Clientes")
    print("2 - Funcionarios")
    print("3 - Contas")
    print("4 - Atendimentos")
    print("5 - Tipos de contas")
    print("0 - Voltar")

def menuRelatorios():
    print("Relatorios")
    print("Escolha a opção desejada:")
    print("1 - Contas de clientes")
    print("2 - Atendimentos por funcionário")
    print("3 - Funcionarios que são clientes")
    print("0 - Voltar")

conn = psycopg2.connect("dbname=Banco user=postgres password=123")

cursor = conn.cursor()



menu()
opcao = int(input("Digite sua opção: "))

while opcao != 0:
    if opcao == 1:
        print("Exibir")
        menuExibir()
        opcaoExibir = int(input("Digite sua opcao: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                cursor.execute('SELECT * FROM clientes')
                query = cursor.fetchall()
                header = ['CPF', 'Numero Agencia', 'Nome', 'Cidade', 'Telefone']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 2:
                cursor.execute('SELECT * FROM funcionarios')
                query = cursor.fetchall()
                header = ['Matricula', 'Nome', 'CPF', 'Salario', 'Funcao']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 3:
                cursor.execute('SELECT * FROM contas')
                query = cursor.fetchall()
                header = ['Numero Conta', 'Limite', 'Tipoconta', 'CPF']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 4:
                cursor.execute('SELECT * FROM atendimentos')
                query = cursor.fetchall()
                header = ['Numero do Atendimento', 'Data', 'CPF do Cliente', 'Matricula do Funcionario', 'Motivo']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 5:
                cursor.execute('SELECT * FROM tipoconta')
                query = cursor.fetchall()
                header = ['Cod. Tipo', 'Limite Maximo', 'Nome do Tipo']
                print(tabulate(query, headers=header))
            else:
                print("Opção invalida!")
            
            menuExibir()
            opcaoExibir = int(input("Digite sua opcao: "))

    if opcao == 2:
        print("Cadastrar")
        menuExibir()
        opcaoExibir = int(input("Digite sua opcao: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                cpf = int(input("CPF: "))
                nroagencia = int(input("Numero agencia: "))
                nome = input("Nome: ")
                fone = input("Telefone: ")
                cidade = input("Cidade: ")
                cursor.execute("INSERT INTO clientes (cpf, nroagencia, nome, cidade, telefone) VALUES ('%s', '%s', %s, %s, %s);", (cpf, nroagencia, nome, cidade, fone))
                conn.commit()
            elif opcaoExibir == 2:
                matricula = input("Matricula: ")
                nome = input("Nome: ")
                cpf = input("CPF: ")
                salario = input("Salario: ")
                funcao = input("Função: ")
                cursor.execute("INSERT INTO funcionarios (matricula, nome, cpf, salario, funcao) VALUES (%s, %s, %s, %s, %s);", (matricula, nome, cpf, salario, funcao))
                conn.commit()
            elif opcaoExibir == 3:
                nrconta = input("Numero da conta: ")
                limite = input("Limite: ")
                tipoconta = input("Tipo da conta: ")
                cpf = input("CPF do cliente: ")
                cursor.execute("INSERT INTO contas (nroconta, limite, tipoconta, cpf) VALUES (%s, %s, %s, %s);", (nrconta, limite, tipoconta, cpf))
                conn.commit()
            elif opcaoExibir == 4:
                nroatendimento = input("Numero do atendimento: ")
                data = input("Data (DD/MM/AAAA)")
               # ano = input("Ano do atendimento: ")
                #mes = input("Mes do atendimento: ")
                #dia = input("Dia do atendimento: ")
                #horario = input("Hora do atendimento(utilize o formato HH:MM): ").split()
                #for horarios in horario:
                #    hora, minutos = [int(i) for i in horarios.split(":")]
               # print(hora)
               # print('oi')
               # print(minutos)
                cpfcliente = input("CPF do Cliente: ")
                matriculafunc = input("Matricula do Funcionario: ")
                motivo = input("Motivo do chamado: ")
                cursor.execute("INSERT INTO atendimentos (nroatendimento, data, cpfcliente, matriculafuncionario, motivo) VALUES (%s, %s, %s, %s, %s);", (nroatendimento, data, cpfcliente, matriculafunc, motivo))
                conn.commit()
            elif opcaoExibir == 5:
                codtipo = input("Codigo do Tipo: ")
                limitemax = input("Limite Maximo: ")
                tipocontanome = input("Nome do Tipo: ")
                cursor.execute("INSERT INTO tipoconta (codtipo, limitemaximo, nometipo) VALUES (%s, %s, %s);", (codtipo, limitemax, tipocontanome))
                conn.commit()
            else:
                print("Opção invalida!")
            
            menuExibir()
            opcaoExibir = int(input("Digite sua opcao: "))

    if opcao == 3:
        print("Remover")  
        menuExibir()
        opcaoExibir = int(input("Digite sua opcao: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                chave = int(input("Digite o CPF do cliente a ser excluído: "))
                query = "DELETE FROM clientes WHERE cpf = %s"
                cursor.execute("DELETE FROM clientes WHERE cpf=%s", (chave,))
                conn.commit()
                        
            elif opcaoExibir == 2:
                chave = int(input("Digite a matricula do funcionario a ser excluído: "))
                cursor.execute("DELETE FROM funcionarios WHERE matricula=%s", (chave,))
                conn.commit()
            elif opcaoExibir == 3:
                chave = int(input("Digite o numero da conta a ser excluída: "))
                cursor.execute("DELETE FROM contas WHERE nroconta=%s", (chave,))
                conn.commit()
            elif opcaoExibir == 4:
                chave = int(input("Digite o numero do atendimento a ser excluído: "))
                cursor.execute("DELETE FROM atendimentos WHERE nroatendimento=%s", (chave,))
                conn.commit()
               
            elif opcaoExibir == 5:
                chave = int(input("Digite o numero do tipo de conta a ser excluído: "))
                cursor.execute("DELETE FROM tipoconta WHERE codtipo=%s", (chave,))
                conn.commit()
               
            else:
                print("Opção invalida!")
            
            menuExibir()
            opcaoExibir = int(input("Digite sua opcao: "))

    if opcao == 4:
        print("Editar")
        menuExibir()
        opcaoExibir = int(input("Digite sua opcao: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                chave = int(input("Digite o CPF do cliente a ser alterado: "))
                nroagencia = int(input("Numero agencia: "))
                nome = input("Nome: ")
                fone = input("Telefone: ")
                cidade = input("Cidade: ")
                cursor.execute("UPDATE clientes SET nroagencia = %s, nome = %s, cidade = %s, telefone = %s WHERE cpf = %s", (nroagencia, nome, cidade, fone, chave))
                conn.commit()
                        
            elif opcaoExibir == 2:
                chave = int(input("Digite a matricula do funcionario a ser alterado: "))
                nome = input("Nome: ")
                salario = input("Salario: ")
                funcao = input("Função: ")
                cursor.execute("UPDATE funcionarios SET nome = %s, salario = %s, funcao = %s WHERE matricula = %s", (nome, salario, funcao, chave))
                conn.commit()

            elif opcaoExibir == 3:
                chave = int(input("Digite o numero da conta a ser alterada: "))
                limite = input("Limite: ")
                tipoconta = input("Tipo da conta: ")
                cursor.execute("UPDATE contas SET limite = %s, tipoconta = %s WHERE nroconta = %s", (limite, tipoconta, chave))
                conn.commit()

            elif opcaoExibir == 4:
                chave = int(input("Digite o numero do atendimento a ser alterado: "))
                data = input("Data(DD/MM/AAAA): ")
                motivo = input("Motivo: ")
                cursor.execute("UPDATE atendimentos SET data = %s, motivo = %s WHERE nroatendimento = %s", (data, motivo, chave))
                conn.commit()
               
            elif opcaoExibir == 5:
                chave = int(input("Digite o codigo do tipo de conta a ser alterado: "))
                limitemax = input("Limite Maximo: ")
                nomeTipo = input("Nome do tipo")
                cursor.execute("UPDATE tipoconta SET limitemaximo = %s, nometipo = %s WHERE codtipo = %s", (limitemax, nomeTipo, chave))
                conn.commit()
            else:
                    print("Opção invalida!")
                
            menuExibir()
            opcaoExibir = int(input("Digite sua opcao: "))

    if opcao == 5:
        print("Relatórios")
        menuRelatorios()
        opcaoExibir = int(input("Digite sua opcao: "))
        while opcaoExibir != 0:
            if opcaoExibir == 1:
                chave = input("Digite o CPF do cliente a ser pesquisado: ")
                cursor.execute('SELECT co.nroconta, co.limite, co.tipoconta FROM contas co JOIN clientes cl ON co.cpf = cl.cpf WHERE co.cpf = %s',(chave,))
                query = cursor.fetchall()
                header = ['Numero conta', 'Limite', 'Tipo conta']
                print(tabulate(query, headers=header))
            elif opcaoExibir == 2:
                chave = input("Digite a matricula do funcionário a ser pesquisado: ")
                cursor.execute('SELECT a.nroatendimento, a.data, a.cpfcliente, a.motivo FROM atendimentos a JOIN funcionarios f ON a.matriculafuncionario = f.matricula WHERE f.matricula = %s',(chave,))
                query = cursor.fetchall()
                header = ['Numero atendimento', 'Data', 'CPF Cliente', 'Motivo de chamado']
                print(tabulate(query, headers=header))
                
            elif opcaoExibir == 3:
                cursor.execute('select f.nome, f.cpf, f.funcao FROM funcionarios f JOIN clientes c ON f.cpf = c.cpf')
                query = cursor.fetchall()
                header = ['Nome', 'CPF', 'Função']
                print(tabulate(query, headers=header))

            else:
                print("Opção invalida!")
            
            menuExibir()
            opcaoExibir = int(input("Digite sua opcao: ")) 


    menu()
    opcao = int(input("Digite sua opção: "))  






     #   cursor.execute('SELECT * FROM clientes WHERE nome = %s', (tabela,))
      #  query = cursor.fetchall()
       # print(query)
 #   else:
  #      print("Opção invalida!")









