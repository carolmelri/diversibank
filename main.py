from cliente import Cliente
from gerente import Gerente
from corrente import Corrente
from poupanca import Poupanca
from endereco import Endereco
import util

""" teste = Cliente("123.123.123-00", "Teste", "teste@teste.com", "(21)999121212", 5000.0)

endereco_teste = Endereco()
endereco_teste.logradouro = "Rua das Flores"
endereco_teste.numero = "15 Fundos"
endereco_teste.bairro = "Centro"
endereco_teste.cidade = "Rio de Janeiro"
endereco_teste.uf = "RJ"
endereco_teste.cep = "12345-000"

if util.valida_sigla_estado(endereco_teste.uf):
  teste.endereco = endereco_teste

print(teste.endereco.uf) """

clientes = []
while True:

  print("-----Diversibank-----")
  print("[A]dicionar")
  print("[E]ditar")
  print("[D]eletar")
  print("[V]isualizar todes")
  print("[C]riar conta corrente")
  print("[S]air")

  op = input("Digite uma opção: ")

  if op.upper() == "A":
    #cpf, nome, email, celular, renda
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome d cliente: ")
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
    posicao = 0
    for cliente in clientes:
      # TODO tratar a lista de clientes vazia
      print("%d: %s - %s" % (posicao, cliente.cpf, cliente.nome))
      posicao += 1
  elif op.upper() == "C":
    # TODO tratar a lista de clientes vazia
    posicao = 0
    for cliente in clientes:
      print("%d: %s - %s" % (posicao, cliente.cpf, cliente.nome))
      posicao += 1

    cliente_escolhido = input("Digite o número do cliente: ")

    cliente = clientes[int(cliente_escolhido)]

    # criar a conta
    conta = Corrente("001-0","1")
    # MELHORIA controlar o numero da conta 

    # atrelar ao cliente
    cliente.adicionar_contaa(conta)
    #sobrescrever esse cliente na lista de clientes
    clientes.insert(int(cliente_escolhido), cliente)

    
  elif op.upper() == "S":
    break
  else:
    print("Opção inválida.")