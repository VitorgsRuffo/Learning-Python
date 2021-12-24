# Sometimes there will be classes that are very similar and just differ in some specific aspects.
# Moreover, we might define new classes that are also similar to other already existing classes.

# When that happens it is better to define a generic class (parent class) and then define specific
# classes (child classes) that inherit attributes and behaviour from it.
# Those child classes only have to define attributes/behaviour that are exclusive for them.
# They can even override some inherited behaviour to make it more specific for them.

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"I'm {self.name} and I'm {self.age}")


# Cat inherits attributes and behaviour from Pet
class Cat(Pet):
    def speak(self):
        print(f"I'm {self.name} the cat and I'm {self.age}")


# Dog inherits attributes and behaviour from Pet
class Dog(Pet):
    # In the case where we wanna add more attributes to the child class
    # we can override the inherited init method.
    def __init__(self, name, age, color):
        super().__init__(name, age) #super() references the parent class (Pet), then we call its init method so that
                                    # we don't need to redefine name and age attributes.
        self.color = color

    def speak(self):
        print(f"I'm {self.name} the dog and I'm {self.age}")


p = Pet("Tom", 12)
p.speak()
c = Cat("Tyler", 5)
c.speak()
d = Dog("Carlos", 9, "Brown")
d.speak()
