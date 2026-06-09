class Personagem:
  def __init__(self, nome, forca, classe, vida, agilidade, inteligencia, destreza):
    self.nome = nome
    self.forca = forca
    self.classe = classe
    self.vida = vida
    self.agilidade = agilidade
    self.inteligencia = inteligencia
    self.destreza = destreza

  def mostrar_info(self):
    print(f'Classe: {self.classe}')
    print(f'Força: {self.forca}')

  def pulou(self):
    print(f'{self.classe} pulou')

  def falar(self):
    print(f'{self.classe} falou')

  def defender(self):
    print(f'{self.classe} defendeu')

  def atacar(self):
    print(f'{self.classe} atacou')

  def descancar(self):
    print(f'{self.classe} descansou')

p1 = Personagem('Ezequiel', 10, 'Guerreiro', 100, 5, 3, 2)
p1.mostrar_info()