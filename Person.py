class Person:
    species = "Human"  # Class Variables

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"This person has name: {self.name} and age: {self.age}")


person1 = Person("Minh", 12)
person2 = Person("Marry", 13)
person1.display_info()
person2.display_info()
print(person2.species)  # Human
print(person1.species)  # Human
print(person1.age)  # 12
print(person2.age)  # 13
