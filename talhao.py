##Criando Classe - Talhões  
class Talhoes:
  #criando o Contrutor da classe
  def __init__(self, id, nome, localizacao, proprietario):
    self.id = id
    self.nome = nome
    self.localizacao = localizacao
    self.proprietario = proprietario


##Metodo de Impressão
  def print(self):
    print('\n--Lista de Talhões--')
    print(f'id.........................: {self.id}')
    print(f'nome.......................: {self.nome}')
    print(f'localizacao................: {self.localizacao}')
    print('\n-------------')

  ##Metodo da Classe