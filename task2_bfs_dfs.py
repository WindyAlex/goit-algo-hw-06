from collections import deque
from graph import create_graph


def dfs_path(G, start, goal):
    visited = set()
    stack = [start]
    parent = {start: None}

    while stack:
        v = stack.pop()

        if v in visited:
            continue

        visited.add(v)

        if v == goal:
            break

        neighbors = list(G.neighbors(v))
        neighbors.sort(reverse=True)

        for n in neighbors:
            if n not in visited and n not in parent:
                parent[n] = v
                stack.append(n)

    if goal not in parent:
        return None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]


def bfs_path(G, start, goal):
    visited = set()
    queue = deque([start])
    parent = {start: None}

    while queue:
        v = queue.popleft()

        if v in visited:
            continue

        visited.add(v)

        if v == goal:
            break

        neighbors = list(G.neighbors(v))
        neighbors.sort()

        for n in neighbors:
            if n not in visited and n not in parent:
                parent[n] = v
                queue.append(n)

    if goal not in parent:
        return None

    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]


def main():
    G = create_graph()

    start = "Server1"
    goal = "Server5"

    dfs_result = dfs_path(G, start, goal)
    bfs_result = bfs_path(G, start, goal)

    print("Task 2: DFS and BFS paths")
    print("Start:", start)
    print("Goal:", goal)

    print("\nDFS path:", dfs_result)
    print("BFS path:", bfs_result)


main()
