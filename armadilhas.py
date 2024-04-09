##Criando Classe - Armadilhas  
class Armadilhas:
  #criando o Contrutor da classe
  def __init__(self, id, nome, localizacao):
    self.id = id
    self.nome = nome
    self.localizacao = localizacao


##Metodo de Impressão
  def print(self):
    print('\n--Lista de Armadilhas--')
    print(f'id................: {self.id}')
    print(f'nome..............: {self.nome}')
    print(f'localização..............: {self.localizacao}')
    print('\n-------------')

  ##Metodo da Classe