import heapq

class Node:
def **init**(self, position, parent=None):
self.position = position
self.parent = parent
self.g = 0
self.h = 0
self.f = 0

```
def __lt__(self, other):
    return self.f < other.f
```

def heuristic(a, b):
# Manhattan Distance
return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, end):
open_list = []
closed_set = set()

```
start_node = Node(start)
heapq.heappush(open_list, start_node)

while open_list:
    current_node = heapq.heappop(open_list)
    closed_set.add(current_node.position)

    if current_node.position == end:
        path = []
        while current_node:
            path.append(current_node.position)
            current_node = current_node.parent
        return path[::-1]

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    for move in neighbors:
        node_pos = (
            current_node.position[0] + move[0],
            current_node.position[1] + move[1]
        )

        # Check boundaries
        if (node_pos[0] < 0 or node_pos[0] >= len(grid) or
            node_pos[1] < 0 or node_pos[1] >= len(grid[0])):
            continue

        # Check obstacle
        if grid[node_pos[0]][node_pos[1]] == 1:
            continue

        if node_pos in closed_set:
            continue

        neighbor = Node(node_pos, current_node)
        neighbor.g = current_node.g + 1
        neighbor.h = heuristic(node_pos, end)
        neighbor.f = neighbor.g + neighbor.h

        heapq.heappush(open_list, neighbor)

return None
```
