from pragas import Praga


class Leitura:
  #método construtor, iniciliza o objeto leitura
  def __init__(self):
    self.safra:Safra = None #singular = 1 elemento
    self.pragas: List<Praga> = []
    self.armadilha: None

  def inserir_praga(self, praga: Praga):
    self.pragas.append(praga)
    
  def exportar_csv():
    pass
