
is_tall = True

if is_tall:
    print("You're tall.")
else:
    print("You're short.")

#boolean operators: or, and, not()


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(1, 2, 3))
print(max_num(100, 2, 3))
print(max_num(1, 200, 3))
