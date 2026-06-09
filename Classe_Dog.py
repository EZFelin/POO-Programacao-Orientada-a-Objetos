class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class PetFactory:
    @staticmethod
    def get_pet(pet_type):
        pets = {'dog': Dog(), 'cat': Cat()}
        return pets[pet_type]

pet = PetFactory.get_pet('dog')
print(pet.speak())  # Woof!