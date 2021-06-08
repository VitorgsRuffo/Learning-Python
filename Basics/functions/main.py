
def say_hi(name, age):
    print("Hello " + name)
    print("You are " + str(age) + " years old.\n")


say_hi("Vitor", 19)
say_hi("Brian", 25)
say_hi("John", 71)


def square(number):
    print("Squaring " + str(number) + "...")
    result = number * number
    return result


print(square(1))
print(square(2))
print(square(3))
print(square(4))

