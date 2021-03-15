from conta import Conta

class Corrente(Conta):

  limite = 0.0

  def __init__(self, numero, agencia):
    super().__init__(numero, agencia)

  def obter_saldo_disponivel_para_operacao(self):
    print('Seu saldo é de R$ %.2f' % self.saldo)
    print('Seu limite é de R$ %.2f' % self.limite)
    print("Saldo disponível para operação: R$ %.2f" (self.saldo + self.limite))
    return limite + saldo

  def depositar(self, valor):
    self.saldo = self.saldo + valor
    print("Valor depositado com sucesso! Saldo atual: R$ %.2f" % self.saldo)

  def sacar(self, valor):
    self.saldo = self.saldo - valor
    print("Saque realizado com sucesso! Saldo atual: R$ %.2f" % self.saldo)
