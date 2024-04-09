  ##Criando Classe - Pragas
from defensivos import Defensivos

class Pragas:
  #criando o Contrutor da classe
  def __init__(self,classificacao, nome_cientifico, cultura, nome_vulgar, ordem, familia, sintomas, bioecologia, controle, mecanismo):
    self.classificacao = classificacao
    self.nome_cientifico = nome_cientifico
    self.cultura = cultura
    self.nome_vulgar = nome_vulgar
    self.ordem = ordem
    self.familia = familia
    self.sintomas = sintomas
    self.bioecologia = bioecologia
    self.controle = controle
    self.defensivos = Defensivos

     
 
##Metodo de Impressão
  def print(self):
    print(f'\n--Lista de Pragas--')
    print(f'Classificacao......: {self.classificacao}')
    print(f'Nome Científico....: {self.nome_cientifico}')
    print(f'Cultura............: {self.cultura}')
    print(f'Nome...............: {self.nome_vulgar}')
    print(f'Ordem..............: {self.ordem}')
    print(f'Familia............: {self.familia}')
    print(f'Controle...........: {self.controle}')
    print(f'Defensivos.........: {self.defensivos}')
    print(f'\n')
    print(f'Sintomas...........: {self.sintomas}')
    print(f'\n')
    print(f'Bioecologia........: {self.bioecologia}')
    print(f'\n-------------')

  ##Metodo da Classe