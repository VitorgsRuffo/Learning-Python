
# Reading: reading information without being able to write to the file.
employees_file = open("employees.txt", "r")
if employees_file.readable():
    # print(employees_file.read())      -> reads the entire file content at once
    # print(employees_file.readline())  -> reads a line moving the file cursor to the next line.
    # print(employees_file.readlines()) -> reads each line and store 'em in an array.
    for employee in employees_file.readlines():
        print(employee)
employees_file.close()

# Appending: adds information to the end of the file. If file doesn't exist it is created.
employees_file = open("employees.txt", "a")
employees_file.write("\nToby - Human Resources")
employees_file.close()

# Writing: overwrites the file information. If file doesn't exist it is created.
employees_file = open("employees2.txt", "w")
employees_file.write("\nKelly - Costumer Service")
employees_file.close()
