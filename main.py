import heapq

# Node class

class Node:
def **init**(self, position, parent=None):
self.position = position
self.parent = parent
self.g = 0  # cost from start
self.h = 0  # heuristic cost
self.f = 0  # total cost

```
def __lt__(self, other):
    return self.f < other.f
```

# Heuristic (Manhattan Distance)

def heuristic(a, b):
return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
open_list = []
closed_set = set()

```
start_node = Node(start)
end_node = Node(end)

heapq.heappush(open_list, start_node)

while open_list:
    current_node = heapq.heappop(open_list)
    closed_set.add(current_node.position)

    # Goal reached
    if current_node.position == end_node.position:
        path = []
        while current_node:
            path.append(current_node.position)
            current_node = current_node.parent
        return path[::-1]

    # Neighbors (4 directions)
    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    for new_position in neighbors:
        node_position = (
            current_node.position[0] + new_position[0],
            current_node.position[1] + new_position[1]
        )

        # Check bounds
        if (node_position[0] < 0 or node_position[0] >= len(grid) or
            node_position[1] < 0 or node_position[1] >= len(grid[0])):
            continue

        # Check obstacle
        if grid[node_position[0]][node_position[1]] == 1:
            continue

        if node_position in closed_set:
            continue

        neighbor = Node(node_position, current_node)
        neighbor.g = current_node.g + 1
        neighbor.h = heuristic(node_position, end_node.position)
        neighbor.f = neighbor.g + neighbor.h

        heapq.heappush(open_list, neighbor)

return None
```

# Example grid (0 = free, 1 = obstacle)

grid = [
[0, 0, 0, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 0, 0, 0],
[0, 1, 1, 1, 0],
[0, 0, 0, 0, 0]
]

start = (0, 0)
end = (4, 4)

path = astar(grid, start, end)

print("Shortest Path:", path)
