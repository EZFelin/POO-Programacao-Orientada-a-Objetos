# Classe Calculadora que possui os métodos de soma, subtração, multiplicação e divisão.
class Calculadora:
  def somar(self,a,b):
    return a+b
  def subtrair(self,a,b):
    return a-b
  def multi(self,a,b):
    return a*b
  def divid(self,a,b):
    return a/b

calc = Calculadora()
print(calc.somar(10,5)) # Output: 15
print(calc.subtrair(10,5)) # Output: 5
print(calc.multi(10,5)) # Output: 50
print(calc.divid(10,5)) # Output: 2