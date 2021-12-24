# Sometimes we wanna define attributes/methods that are not specific for
# instances of the class.

class Person:
    # class attributes are shared between its instances
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_person()

    # class methods don't operate on class instances.
    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1


p1 = Person("Vitor")
print(Person.number_of_people)
p2 = Person("Tom")
print(Person.number_of_people)
