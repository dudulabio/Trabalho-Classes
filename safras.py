##Criando Classe - Safras  
class Safras:
  #criando o Contrutor da classe
  def __init__(self, nome, periodo):
    self.nome = nome
    self.periodo = periodo


##Metodo de Impressão
  def print(self):
    print('\n--Lista de Safras--')
    print(f'nome................: {self.nome}')
    print(f'periodo..............: {self.periodo}')
    print('\n-------------')

  ##Metodo da Classe