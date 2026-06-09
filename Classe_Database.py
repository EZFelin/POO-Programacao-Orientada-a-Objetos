class DatabaseConnection:
    _instance = None  # Atributo para armazenar a instância única

    def __new__(cls):
        #Garante que tenha apenas uma conexão com a instância
        if cls._instance is None:
            # Caso não exista uma instância, cria uma nova
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            cls._instance._initialize_connection()

        return cls._instance

    def _initialize_connection(self):
        #Simula a conexão com o banco de dados
        self.connection = "Conexão com o banco de dados estabelecida"
        print(self.connection)

    def execute_query(self, query):
        #Simula uma execução de consulta
        print(f"Executando consulta: {query}")

# Testando a implementação

# Criando duas instâncias
db1 = DatabaseConnection()
db2 = DatabaseConnection()

# Verificando se as instâncias são a mesma
print(db1 is db2)  # Deve imprimir: True

# Executando uma consulta com a instância
db1.execute_query("SELECT * FROM usuarios")