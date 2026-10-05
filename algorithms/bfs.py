"""Breadth-first search implementation."""

from collections import deque

from graph import Graph


def breadth_first_search(
    graph: Graph,
    start: str,
    goal: str,
    verbose: bool = False,
) -> tuple[list[str] | None, int]:
    """Find a path by exploring the shallowest nodes first.

    The search ignores edge weights, so it finds a path with the fewest edges.
    For an adjacency-list graph, time complexity is O(V + E) and space
    complexity is O(V), where V is the number of nodes and E is the number of
    edges. Returns (path, expanded node count), or (None, count) if unreachable.
    """
    if start not in graph or goal not in graph:
        return None, 0

    frontier: deque[list[str]] = deque([[start]])
    discovered = {start}
    expanded: set[str] = set()
    expanded_count = 0

    while frontier:
        path = frontier.popleft()
        node = path[-1]

        if verbose:
            print(f"BFS expanding: {node!r}")

        if node == goal:
            if verbose:
                print(f"BFS queue: {list(frontier)}")
                print(f"BFS visited: {sorted(expanded)}")
            return path, expanded_count

        expanded.add(node)
        expanded_count += 1
        for neighbor in graph.get(node, {}):
            if neighbor not in discovered:
                discovered.add(neighbor)
                frontier.append(path + [neighbor])

        if verbose:
            print(f"BFS queue: {list(frontier)}")
            print(f"BFS visited: {sorted(expanded)}")

    return None, expanded_count
