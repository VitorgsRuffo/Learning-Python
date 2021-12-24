# Every variable in python is an instance of some class.
# A class defines how objects (variables) of its type are represented and what operations can be performed on those.

# Those classes are either built-in, like int, str, float
# e.g, By doing this we're instantiating objects of classes str and int, respectively.
x = "hello"
print(type(x))

y = 10
print(type(y))

# Or, they are user-defined classes.
# e.g, defining a new variable (object) type (class):


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        result = 0
        for student in self.students:
            result += student.get_grade()
        return result / len(self.students)


s1 = Student("Vitor", 19, 85)
s2 = Student("Tom", 19, 95)
s3 = Student("Tim", 19, 75)

c1 = Course("Calculus 1", 30)
c1.add_student(s1)
c1.add_student(s2)
print(c1.get_average_grade())

c2 = Course("Calculus 2", 30)
c1.add_student(s1)
c1.add_student(s3)
print(c1.get_average_grade())
