class Personagem:
  def __init__(self, nome, classe, vida, forca, agilidade, inteligencia, vigor, presenca):
    self.nome = nome
    self.classe = classe
    self.vida = vida
    self.forca = forca
    self.agilidade = agilidade
    self.inteligencia = inteligencia
    self.vigor = vigor
    self.presenca = presenca


  def mostrar_info(self):
    print(f'Nome: {self.nome}')
    print(f'Classe: {self.classe}')
    print(f'Vida: {self.vida}')
    print(f'ForÇa: {self.forca}')
    print(f'Agilidade: {self.agilidade}')
    print(f'Inteligência: {self.inteligencia}')
    print(f'Vigor: {self.vigor}')
    print(f'Presença: {self.presenca}')

    def pular(self):
      print(f'{self.nome} pulou')
    def falar(self):
      print(f'{self.nome} falou')
    def defender(self):
      print(f'{self.nome} defendeu')
    def atacar(self):
      print(f'{self.nome} atacou')
    def descansar(self):
        print(f'{self.nome} descansou')

p1 = Personagem("Himaru", "Ocultista", 17, 2, 3, 3, 1, 3)
p1.mostrar_info()
p1.pular()
p1.falar()
p1.defender()
p1.atacar()
p1.descansar()