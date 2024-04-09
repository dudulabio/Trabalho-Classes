##Criando Classe - Defensivos  
class Defensivos:
  #criando o Contrutor da classe
  def __init__(self, produto, mecanismo, titular, formulacao, toxicidade, ambientacao):
    self.produto = produto
    self.mecanismo = mecanismo
    self.titular = titular
    self.formulacao = formulacao
    self.toxicidade = toxicidade
    self.ambientacao = ambientacao

   
##Metodo de Impressão
  def print(self):
    print('\n--Lista de Defensivos--')
    print(f'Produto................: {self.produto}')
    print(f'Mecanismo..............: {self.mecanismo}')
    print(f'Titular................: {self.titular}')
    print(f'Formulacao.............: {self.formulacao}')
    print(f'Toxicidade.............: {self.toxicidade}')
    print(f'Ambientacao............: {self.ambientacao}')
    print('\n-------------')

  ##Metodo da Classe