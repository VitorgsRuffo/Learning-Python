# Class that defines Person data type.
#
# We can create variables (objects) of this new type.
# Moreover, we can operate on these variables (objects)
# using the functions defined in the class.

class Person:

    def __init__(self, name, age, height, job):
        self.name = name
        self.age = age
        self.height = height
        self.job = job

    def self_introduce(self):
        print("Hi, my name is " + self.name + " and I'm " + str(self.age))

    def walk(self):
        print(self.name + " is walking...")

    def run(self):
        print(self.name + " is running...")

    def to_string(self):
        string = "\nName: " + self.name + ".\nAge: " + str(self.age) + ".\nJob: " + self.job
        return string
