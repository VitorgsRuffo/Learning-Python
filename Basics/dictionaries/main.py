# dictionary: collection of key-value pairs.
#             Each key must be unique and is
#             used to access the value
#             associated with it.

stuff = {
    "Jan": "January",
    "Feb": "February",
    "Mar": 3,
    7: "doodad",
    10: 7.1,
    7.9: "float"
}

print(stuff["Jan"])
print(stuff["Feb"])
print(stuff["Mar"])
print(stuff[7])
print(stuff[10])
print(stuff[7.9])

print("When using get to access a dictionary value we can specify a value that is gonna be retuned in case that key doesn't map to any value:")
print(stuff.get("Car", "Key not found."))
