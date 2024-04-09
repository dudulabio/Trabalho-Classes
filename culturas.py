  ##Criando Classe - Culturas  
class Culturas:
    #criando o Contrutor da classe
    def __init__(self, variedades, tipo):
      self.variedades = variedades
      self.tipo = tipo


  ##Metodo de Impressão
    def print(self):
      print('\n--Lista de Armadilhas--')
      print(f'variedades................: {self.variedades}')
      print(f'tipo..............: {self.tipo}')
      print('\n-------------')

    ##Metodo da Classe