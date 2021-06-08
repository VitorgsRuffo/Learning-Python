# Class that defines Student data type.
#
# Student is a Person with some additional features.
# So, it can inherit attributes and behaviour from Person type and just
# specify the extra attributes/behaviour that it needs in order to be a Student.

from Person import Person


class Student(Person):

    def __init__(self, name, age, height, job, major, gpa):
        super().__init__(name, age, height, job)
        self.major = major
        self.gpa = gpa

    def is_on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    # Student has inherited a function that hasn't the exact behaviour that it needs,
    # so, it can overwrite it.
    def to_string(self):
        string = "\nStudent\nName: " + self.name + ".\nMajor: " + self.major + "."
        return string


