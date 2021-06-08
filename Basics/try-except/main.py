# These constructs helps us handle errors that would crash our program.

# example 1: if user enters unexpected data we must be able to handle it.
number = int(input("Enter a number: "))
print(number)

# solution: we try to execute the code in try block. If some error occurs we handle it in except block.
try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input.")

# example 2: there exist all sorts of different errors that would crash the program.
#            We are able to specify which error we want to handle.
#            In this block of code two errors might happen: invalid input or division by zero.
#            So we can create one except block for exclusively dealing with each one of 'em.
#            If we use only a general except block we would handle any error, and that's not a good practice.
try:
    number = int(input("Enter a number: "))
    print(number)
    print(10/number)
except ValueError as err:
    print(err)
except ZeroDivisionError as err:
    print(err)

