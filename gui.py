import tkinter as tk
from astar import astar
from grid import create_grid

CELL_SIZE = 50

class PathfindingGUI:
def **init**(self, root):
self.root = root
self.grid = create_grid()
self.start = (0, 0)
self.end = (4, 4)

```
    self.canvas = tk.Canvas(root, width=250, height=250)
    self.canvas.pack()

    self.draw_grid()

    button = tk.Button(root, text="Run A*", command=self.run_astar)
    button.pack()

def draw_grid(self, path=None):
    self.canvas.delete("all")
    for i in range(len(self.grid)):
        for j in range(len(self.grid[0])):
            x1 = j * CELL_SIZE
            y1 = i * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE

            color = "white"

            if self.grid[i][j] == 1:
                color = "black"
            elif (i, j) == self.start:
                color = "green"
            elif (i, j) == self.end:
                color = "red"
            elif path and (i, j) in path:
                color = "blue"

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

def run_astar(self):
    path = astar(self.grid, self.start, self.end)
    self.draw_grid(path)
```

if **name** == "**main**":
root = tk.Tk()
root.title("A* Pathfinding Visualizer")
app = PathfindingGUI(root)
root.mainloop()
