from collections import deque

def bfs(grid, start, end):
queue = deque()
queue.append((start, [start]))
visited = set()

```
while queue:
    (current, path) = queue.popleft()

    if current == end:
        return path

    if current in visited:
        continue

    visited.add(current)

    neighbors = [(0,1),(0,-1),(1,0),(-1,0)]

    for move in neighbors:
        node = (current[0] + move[0], current[1] + move[1])

        if (node[0] < 0 or node[0] >= len(grid) or
            node[1] < 0 or node[1] >= len(grid[0])):
            continue

        if grid[node[0]][node[1]] == 1:
            continue

        queue.append((node, path + [node]))

return None
```
