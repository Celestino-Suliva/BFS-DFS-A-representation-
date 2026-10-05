"""Iterative depth-first search implementation."""

from graph import Graph


def depth_first_search(
    graph: Graph,
    start: str,
    goal: str,
    verbose: bool = False,
) -> tuple[list[str] | None, int]:
    """Find a path by exploring one branch as deeply as possible.

    The search uses a LIFO stack and ignores edge weights. For an
    adjacency-list graph, time complexity is O(V + E) and space complexity
    is O(V). Returns (path, expanded node count), or (None, count) if
    unreachable.
    """
    if start not in graph or goal not in graph:
        return None, 0

    frontier = [[start]]
    discovered = {start}
    expanded: set[str] = set()
    expanded_count = 0

    while frontier:
        path = frontier.pop()
        node = path[-1]

        if verbose:
            print(f"DFS expanding: {node!r}")

        if node == goal:
            if verbose:
                print(f"DFS stack: {frontier}")
                print(f"DFS visited: {sorted(expanded)}")
            return path, expanded_count

        expanded.add(node)
        expanded_count += 1

        # Reverse insertion order so the first listed neighbor is explored
        # first when paths are popped from the stack.
        for neighbor in reversed(list(graph.get(node, {}))):
            if neighbor not in discovered:
                discovered.add(neighbor)
                frontier.append(path + [neighbor])

        if verbose:
            print(f"DFS stack: {frontier}")
            print(f"DFS visited: {sorted(expanded)}")

    return None, expanded_count
