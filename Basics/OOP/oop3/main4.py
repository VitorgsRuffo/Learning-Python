# Sometimes is a good practice to group related functions together by defining them in a class.
# Those will be called static methods. They don't depend on class intances and can be invoked
# by referencing the class.

class Math:
    @staticmethod
    def add5(number):
        return number + 5

    @staticmethod
    def add10(number):
        return number + 10

    @staticmethod
    def add15(number):
        return number + 15


print(Math.add5(10))
print(Math.add10(10))
print(Math.add15(10))
