class Carro:
  def detalhes(self):
    return "Utiliza gasolina -exceto os elétricos-, veículo de 4 rodas"

class Moto:
  def detalhes(self):
    return "Utiliza gasolina -exeto os elétricos-, veículo de 2 rodas"

class Bicicleta:
  def detalhes(self):
    return "Não utiliza gasolina, utiliza pedal e tem 2 rodas"

class VeiculosFactory:
    @staticmethod
    def get_veiculo(veiculo_type):
        veiculos = {'Carro': Carro(), 'Moto': Moto(), 'Bicicletas:': Bicicleta}
        return veiculos[veiculo_type]

veiculo = VeiculosFactory.get_veiculo('Carro')
print(veiculo.detalhes())

