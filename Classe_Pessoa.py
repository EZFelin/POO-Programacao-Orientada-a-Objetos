# Classe Pessoa que possui os atributos nome, idade, peso e altura, e os métodos calcular_imc, imprimir_dados, imc_string e imc_parametro. 
# Definição de uma classe
class Pessoa:
    # Método construtor, inicializa o objeto
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome  # Atributo nome
        self.idade = idade  # Atributo idade
        self.peso = peso
        self.altura = altura

    def calcular_imc(self):
        return self.peso / (self.altura ** 2)
    def imprimir_dados(self):
      print(f"Nome: {self.nome}")
      print(f"Idade: {self.idade}")

    def imc_string(self):
      imc= self.calcular_imc()
      if imc<17:
        print("Muito abaixo do peso.")
      elif imc>=17 and imc<18.5:
       print("Abaixo do peso.")
      elif imc>=18.5 and imc<25:
       print("Peso normal.")
      elif imc>=25 and imc<30:
       print("Acima do peso.")
      elif imc>=30 and imc<35:
       print("Obesidade 1.")
      elif imc>=35 and imc<40:
        print("Obesidade severa.")
      elif imc>=40:
        print("Obesidade mórbida.")

    def imc_parametro(self,imc):
       if imc<17:
        print("Muito abaixo do peso.")
       elif imc>=17 and imc<18.5:
          print("Abaixo do peso.")
       elif imc>=18.5 and imc<25:
        print("Peso normal.")
       elif imc>=25 and imc<30:
        print("Acima do peso.")
       elif imc>=30 and imc<35:
        print("Obesidade 1.")
       elif imc>=35 and imc<40:
         print("Obesidade severa.")
       elif imc>=40:
         print("Obesidade mórbida.")

# Criando um objeto da classe Pessoa
p1 = Pessoa('João', 25, 70, 1.94)
p2 = Pessoa('Maria', 30, 60, 1.70)
p3 = Pessoa('5', 28, 80, 1.80)
p4 = Pessoa('Ezequiel', 17, 71, 1.75)

imc = p1.calcular_imc()
print(f"O IMC de {p1.nome} é {imc:.2f}")
if imc<17:
  print("Muito abaixo do peso.")
elif imc>=17 and imc<18.5:
  print("Abaixo do peso.")
elif imc>=18.5 and imc<25:
  print("Peso normal.")
elif imc>=25 and imc<30:
  print("Acima do peso.")
elif imc>=30 and imc<35:
  print("Obesidade 1.")
elif imc>=35 and imc<40:
  print("Obesidade severa.")
elif imc>=40:
  print("Obesidade mórbida.")

p1.imprimir_dados()
p1.imc_string()

imc= p2.calcular_imc()
p2.imc_parametro(imc)
