from cliente import Cliente
from gerente import Gerente
from corrente import Corrente
from poupanca import Poupanca
from endereco import Endereco
import util

clientes = []
contas_criadas = 0

while True:

  print("-----Diversibank-----")
  print("[A]dicionar")
  print("[E]ditar")
  print("[D]eletar")
  print("[V]isualizar todes")
  print("[C]riar conta corrente")
  print("De[p]ositar dinheiro")
  print("[S]air")

  op = input("Digite uma opção: ")

  if op.upper() == "A":
    #cpf, nome, email, celular, renda
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    celular = input("Digite o celular: ")
    renda =  input("Digite a renda: ")

    # TODO implementar try/exception - já implementado na classe Cliente
    novo_cliente = Cliente(cpf, nome, email, celular, renda)
    clientes.append(novo_cliente)

    # MELHORIA: verificar na lista de clientes se já existe u cliente com aquele cpf cadastrado
  elif op.upper() == "E":
    print("Editar")
  elif op.upper() == "D":
    print("Deletar")
  elif op.upper() == "V":
    util.exibir_lista_de_clientes(clientes)
  elif op.upper() == "C":
    util.exibir_lista_de_clientes(clientes)

    cliente_escolhido = input("Digite o número do cliente: ")

    indice = int(cliente_escolhido)
    cliente = clientes[indice]
    print(cliente.cpf)
    conta = Corrente(str(contas_criadas + 1), "001")
    # atrelar ao cliente
    cliente.adicionar_conta(conta)
    #remove o cliente da lista
    clientes.pop(indice)
    #insere de novo na mesma posição com as informações atualizadas
    clientes.insert(indice, cliente)
  
  elif op.upper() == "P":
    util.exibir_lista_de_clientes(clientes)
    cliente_escolhido = input("Digite o número do cliente: ")
    conta = clientes[int(cliente_escolhido)].contas[0]

    valor = input("Digite o valor a ser depositado: ")
    conta.depositar(float(valor))
    
  elif op.upper() == "S":
    break
  else:
    print("Opção inválida.")