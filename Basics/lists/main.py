
stuff = ["Tree", False, 7.9876, 10]
print(stuff)
print("\n\n" + stuff[0])
print("\n\n" + str(stuff[1]))
print("\n\n" + str(stuff[2]))
print("\n\n" + str(stuff[3]))

print("\n\nWe can access the list from its end by using negative indices starting at -1:\n")
print("\n\n" + str(stuff[-1]))
print("\n\n" + str(stuff[-2]))
print("\n\n" + str(stuff[-3]))
print("\n\n" + stuff[-4])

print("\n\nAcessing all elements from ith(i=1) index onwards:")
print(stuff[1:])

print("\n\nAcessing all elements from ith till j-1th index:")
print(stuff[1:3])

print("\n\nModifying list elements:")
stuff[1] = True
stuff[0] = 9
print(stuff)

#1:10:45
