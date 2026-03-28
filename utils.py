def print_grid(grid, path=None):
for i in range(len(grid)):
for j in range(len(grid[0])):
if path and (i, j) in path:
print("P", end=" ")
elif grid[i][j] == 1:
print("#", end=" ")
else:
print(".", end=" ")
print()
