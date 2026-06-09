class Publisher: #Classe de publicidade
    def __init__(self): #Método construtor, constroi o código
        self.subscribers = [] #Vetor

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber) #Append adiciona no vetor

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message) #Atualiza

class Subscriber: #Objeto do inscrito
    def __init__(self, name): #Metodo contrutor
        self.name = name

    def update(self, message): #Atualiza
        print(f"{self.name} recebeu: {message}")

publisher = Publisher() # Intanciaçâo / mesmo que igualar, so que é no POO
subscriber1 = Subscriber("Alice")
subscriber2 = Subscriber("Bob")

publisher.subscribe(subscriber1)
publisher.subscribe(subscriber2)

publisher.notify("Olá, Observers!")# Chamada da notificação