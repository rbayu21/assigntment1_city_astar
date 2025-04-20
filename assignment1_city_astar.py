import heapq
import math
import time


def euclidean(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def a_star(city, roads, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g = {c: float('inf') for c in city}
    g[start] = 0
    f = {c: float('inf') for c in city}
    f[start] = euclidean(city[start], city[goal])
    node_count = 1

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct(came_from, start, goal), node_count

        for neighbor in roads[current]:
            temp_g = g[current] + euclidean(city[current], city[neighbor])
            if temp_g < g[neighbor]:
                came_from[neighbor] = current
                g[neighbor] = temp_g
                f[neighbor] = temp_g + euclidean(city[neighbor], city[goal])
                heapq.heappush(open_set, (f[neighbor], neighbor))
                node_count += 1
    return None, node_count


def gbfs(city, roads, start, goal):
    open_set = [(euclidean(city[start], city[goal]), start)]
    came_from = {}
    visited = set()
    node_count = 1

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            return reconstruct(came_from, start, goal), node_count

        visited.add(current)
        for neighbor in roads[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                came_from[neighbor] = current
                heapq.heappush(open_set, (euclidean(city[neighbor], city[goal]), neighbor))
                node_count += 1
    return None, node_count


def reconstruct(came_from, start, goal):
    path = [goal]
    while path[-1] != start:
        path.append(came_from[path[-1]])
    path.reverse()
    return path


def run_assignment1():
    city = {
        "A": (0, 0), "B": (2, 1),
        "C": (4, 2), "D": (5, 5),
        "E": (1, 4)
    }

    roads = {
        "A": ["B", "E"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C"],
        "E": ["A", "D"]
    }

    start, goal = "A", "D"

    print("\nAssignment 1 - A* and GBFS Path (City Navigation):")

    t0 = time.perf_counter()
    a_path, a_nodes = a_star(city, roads, start, goal)
    t1 = time.perf_counter()
    print("A* Path:", " -> ".join(a_path) if a_path else "No path found")
    print(f"A* Time: {(t1 - t0)*1000:.4f} ms | Nodes Explored: {a_nodes}")

    t0 = time.perf_counter()
    g_path, g_nodes = gbfs(city, roads, start, goal)
    t1 = time.perf_counter()
    print("GBFS Path:", " -> ".join(g_path) if g_path else "No path found")
    print(f"GBFS Time: {(t1 - t0)*1000:.4f} ms | Nodes Explored: {g_nodes}")
