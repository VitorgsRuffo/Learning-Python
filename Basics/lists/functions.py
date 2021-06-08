integers = [1, 4, 6, 8]
floats = [1.3, 4.3, 2.1]
strings = ["me", "he", "she"]
print(integers)
print(floats)
print(strings)

print("\n\nappending a list to another one:")
floats.extend(integers)
print(floats)

print("\n\nappending an element to a list:")
strings.append("it")
print(strings)

print("\n\nadding an element to a list:")
integers.insert(1, 11)
print(integers)

print("\n\nremoving an element from a list:")
floats.remove(4.3)
print(floats)

print("\n\nremoving all elements from a list:")
integers.clear()
print(integers)

print("\n\nfinding the index of a list element:")
print(strings.index("she"))
strings.remove("he")
#print(strings.index("he"))

print("\n\ncounting how many elements with a certain value exist in the list:")
strings.insert(0, "me")
strings.insert(2, "me")
print(strings)
print(strings.count("me"))

print("\n\nsorting a list in ascending order:")
print(floats)
floats.sort()
print(floats)

print("\n\ncreating a copy of a list:")
floats2 = floats.copy()
print(floats2)