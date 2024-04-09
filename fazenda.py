class Fazenda:
  def __init__(self, nome, area, proprietario):
    self.nome = nome
    self.area = area
    self.proprietario = proprietario
    self.defensivos = []
    self.pragas = []
    
  def imprimirListaDefensivos(self):
    for t in self.defensivos:
      t.print()
    
  def  addDefensivosLista(self,Defensivos):
    self.defensivos.append(Defensivos)
    

  def  removeDefensivosLista(self,Defensivos):
    self.defensivos.remove(Defensivos)

  def imprimirListaPragas(self):
    for p in self.pragas:
      p.print()


  def  addPragasLista(self,Pragas):
    self.pragas.append(Pragas)


  def  removePragasLista(self,Pragas):
    self.pragas.remove(Pragas)


