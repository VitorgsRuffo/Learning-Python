
#2-dimensional lists:

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(number_grid[0][0])
print(number_grid[1][1])
print(number_grid[2][2])
print(number_grid[0][2])

print("Printing a two-dimensional array using nested for loops:")
for row in number_grid:
    for col in row:
        print(col)
