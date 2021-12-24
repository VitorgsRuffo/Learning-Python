#Topics: inheritance, method overriding

from Person import Person
from Student import Student

me = Student("Vitor", 19, 2.2, "none", "CS", 3.6)
she = Student("Pamela", 22, 1.75, "Business intern", "Business", 3.9)
he = Person("Tom", 21, 1.8, "Carpenter")

print(me)
print(me.self_introduce())
print(me.name)
print(me.major)
print(me.gpa)
print("Is " + me.name + " on the honor roll? " + str(me.is_on_honor_roll()))

print(she.to_string())

print(he.to_string())

