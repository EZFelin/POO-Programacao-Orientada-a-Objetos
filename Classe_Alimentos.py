class Alimentos:
    def __init__(self, setor, nome, estoque):
        self.setor = setor
        self.nome = nome
        self.estoque = estoque

    def mostrar_info(self):
        print(f'Setor: {self.setor}')
        print(f'Nome: {self.nome}')
        print(f'Estoque: {self.estoque}')

class Queijo(Alimentos):
    def __init__(self, setor, nome, estoque, marca, tipoqueijo, quantidade):
        super().__init__(setor, nome, estoque)
        self.marca = marca
        self.tipoqueijo = tipoqueijo
        self.quantidade = quantidade

    def mostrar_info(self):
        super().mostrar_info()
        print(f'Marca: {self.marca}')
        print(f'Tipo de queijo: {self.tipoqueijo}')
        print(f'Quantidade atual: {self.quantidade}')

class Setores:
    def __init__(self):
        self.marcas = []
        self.queijos = []

    def adicionar_marca(self, produto):
        if hasattr(produto, 'marca'):
            self.marcas.append(produto.marca)

    def adicionar_queijo(self, produto):
        if isinstance(produto, Queijo):
            self.queijos.append(produto)

    def mostrar_queijo(self):
        print('--- Queijos ---')
        for queijo in self.queijos:
            queijo.mostrar_info()
            print('')

setores = Setores()

queijo = Queijo('Lactícios', 'Queijo', 40, 'Président', 'Grana Padano', 10)
produto1 = Alimentos('Lactícios', 'Queijo', 40)

setores.adicionar_marca(queijo)
setores.adicionar_queijo(queijo)
setores.mostrar_queijo()