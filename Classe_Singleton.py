class Singleton:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(Singleton, cls).__new__(cls)
        return cls.__instance

obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True