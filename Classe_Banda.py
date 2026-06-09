# instrumento.py
class Instrumento:
    def __init__(self, nome, tipo, cor):
       self.nome = nome
       self.tipo = tipo
       self.cor = cor

    def mostrar_info(self):
      print(f'Instrumento: {self.nome}, Tipo: {self.tipo} Cor: {self.cor}')

# instrumento.py (continuado)
class Guitarra(Instrumento):
    def __init__(self, nome, tipo, cor, num_cordas):
       super().__init__(nome, tipo, cor)
       self.num_cordas = num_cordas
    def mostrar_info(self):
       super().mostrar_info()
       print(f'Número de Cordas: {self.num_cordas}')

class Bateria(Instrumento):
    def __init__(self, nome, tipo, cor, num_tambores):
       super().__init__(nome, tipo, cor)
       self.num_tambores = num_tambores
    def mostrar_info(self):
       super().mostrar_info()
       print(f'Número de Tambores: {self.num_tambores}')

class Musico:
    def __init__(self, nome, instrumento):
       self.nome = nome
       self.instrumento = instrumento

    def mostrar_info(self):
       print(f'Músico: {self.nome}')
       self.instrumento.mostrar_info()

# banda.py
class Banda:
    def __init__(self, nome):
       self.nome = nome
       self.musicos = []
       self.albuns = []

    def adicionar_musico(self, musico):
       self.musicos.append(musico)

    def adicionar_album(self, album):
      self.albuns.append(album)

    def remover_album(self, album):
      self.albuns.remove(album)

    def mostrar_musicos(self):
       print(f'Banda: {self.nome}')
       for musico in self.musicos:
         musico.mostrar_info()

# album.fy
class Album:
  def __init__(self, titulo, ano):
    self.titulo = titulo
    self.ano = ano
    self.faixa = []

  def adicionar_faixa(self,faixa):
      self.faixa.append(faixa)

  def remover_faixa(self,faixa):
      self.faixa.remove(faixa)

# Criando instrumentos
guitarra = Guitarra('Fender Stratocaster', 'Cordas', 'Vermelho', 6,)
bateria = Bateria('Yamaha Stage Custom', 'Percussão', 'Azul', 5)

# Criando músicos com instrumentos
musico1 = Musico('John', guitarra)
musico2 = Musico('Ringo', bateria)

album1 = Album('Abbey Road', 1969)
album2 = Album('Dark Side of the Moon', 1973)

album1.adicionar_faixa('Come Together')
album1.adicionar_faixa('Something')
album2.adicionar_faixa('Speak to Me')
album2.adicionar_faixa('Breathe')

# Criando banda e adicionando músicos
banda = Banda('The Beatles')
banda.adicionar_musico(musico1)
banda.adicionar_musico(musico2)
banda.adicionar_album(album1)
banda.adicionar_album(album2)

# Exibindo informações da banda
banda.mostrar_musicos()
