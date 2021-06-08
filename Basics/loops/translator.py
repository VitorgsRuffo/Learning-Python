# In bird language every vowel becomes a 'b':
# e.g, I have a dog -> B hbvb b dbg


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "B"
            else:
                translation += "b"
        else:
            translation += letter
    return translation


print(translate(input("Enter a phrase: ")))
