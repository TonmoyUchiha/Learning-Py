#Py uses classes to define record type

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("John Doe", 30)
print("Name:", person1.name)
print("Age:", person1.age)
