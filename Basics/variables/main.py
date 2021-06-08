#variables:

person_name = "Vitor"
person_age = 19
person_age_string = "19"
person_wallet = 0.0012
is_tall = True
is_rich = False
print(person_name + " is " + person_age_string + " years old.")
person_name = "Gabriel"
print("That guy's got a new name: " + person_name)


#data types:

#strings:
print("\n\nStrings: ")
sentence = "\nHello guys"
print("\"using quotation marks\"")
print(sentence)
print(sentence.lower())
print(sentence.upper())
print(sentence.upper().isupper())
print("\nsentence length:")
print(len(sentence))
print(sentence[1])
print(sentence[10])
print(sentence.index("H"))
print(sentence.index("gu"))
print(sentence.replace("guys", "everybody"))

#numbers:
from math import * #importing math module functions
print("\n\nNumbers:")
print(-2)
print(5.71112)
num = (4 * (3 + 2))/2 - 5
print(num)
print("num = " + str(num))
num2 = -10
num2 = abs(num2)
print(num2)
num2 = pow(num2, 3)
print(num2)
print(max(11, 7))
print(min(11, 7))
print(round(5.4))
print(round(5.5))
print(floor(7.4))
print(ceil(7.4))
print(sqrt(9))