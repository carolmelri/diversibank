def valida_sigla_estado(uf):
  UFs = ("AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO")
  # procurar um objeto dentro de uma tupla
  # neste caso, o objeto é uf, que é uma string
  if uf in UFs:
    return True
  else:
    return False

def exibir_lista_de_clientes(clientes):
  if len(clientes) == 0:
    print("Nenhum cliente cadastrado!")
  else:
    posicao = 0
    for cliente in clientes:
      print("%d: %s - %s" % (posicao, cliente.cpf, cliente.nome))
      posicao += 1 