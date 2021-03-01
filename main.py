from cliente import Cliente
from gerente import Gerente
from corrente import Corrente
from poupanca import Poupanca
from endereco import Endereco
import util

teste = Cliente("123.123.123-00", "Teste", "teste@teste.com", "(21)999121212", 5000.0)

endereco_teste = Endereco()
endereco_teste.logradouro = "Rua das Flores"
endereco_teste.numero = "15 Fundos"
endereco_teste.bairro = "Centro"
endereco_teste.cidade = "Rio de Janeiro"
endereco_teste.uf = "RJ"
endereco_teste.cep = "12345-000"

if util.valida_sigla_estado(endereco_teste.uf):
  teste.endereco = endereco_teste

print(teste.endereco.uf)