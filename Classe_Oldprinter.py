class OldPrinter:

  def Old_Print(self):
    return "Oie"

class Adapter:

  def __init__(self,novo):
        self.novo = novo

  def Old_Print(self):
    return f"Adaptado de {self.novo.Old_Print()} para Olá"

old_printe = OldPrinter()
adapter = Adapter(old_printe)

print(adapter.Old_Print())