
num1 = float(input("Enter first number:"))
operator = input("Enter operation:")
num2 = float(input("Enter second number:"))

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    print(num1/num2)
else:
    print("Operation not supported.")