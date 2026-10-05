"""A* search implementation."""

import heapq
from itertools import count

from graph import Graph


def a_star_search(
    graph: Graph,
    start: str,
    goal: str,
    heuristic: dict[str, float],
    verbose: bool = False,
) -> tuple[list[str] | None, float | None, int]:
    """Find a minimum-cost path using f(n) = g(n) + h(n).

    A min-heap selects the node with the lowest estimated total cost. With an
    admissible heuristic and non-negative edge costs, A* is optimal. A
    straightforward bound is O((V + E) log V) time and O(V + E) space;
    reopening nodes on improved paths may increase work for inconsistent
    heuristics. Returns (path, total cost, expanded node count), or
    (None, None, count) if unreachable.
    """
    if start not in graph or goal not in graph:
        return None, None, 0

    tie_breaker = count()
    frontier: list[tuple[float, int, str]] = [
        (heuristic.get(start, 0), next(tie_breaker), start)
    ]
    came_from: dict[str, str] = {}
    g_cost: dict[str, float] = {start: 0}
    expanded_cost: dict[str, float] = {}
    expanded_count = 0

    while frontier:
        _, _, node = heapq.heappop(frontier)
        current_cost = g_cost[node]

        # Ignore an outdated heap entry or a node already expanded at a
        # better cost.
        if current_cost >= expanded_cost.get(node, float("inf")):
            continue

        if verbose:
            h_value = heuristic.get(node, 0)
            print(
                f"A* expanding: {node!r} (g={current_cost}, h={h_value}, "
                f"f={current_cost + h_value})"
            )

        if node == goal:
            path = [goal]
            while path[-1] != start:
                path.append(came_from[path[-1]])
            path.reverse()
            if verbose:
                print(
                    "A* frontier (node, f): "
                    + str([(name, score) for score, _, name in sorted(frontier)])
                )
                print(f"A* visited: {sorted(expanded_cost)}")
            return path, current_cost, expanded_count

        expanded_cost[node] = current_cost
        expanded_count += 1

        for neighbor, edge_cost in graph.get(node, {}).items():
            tentative_cost = current_cost + edge_cost
            if tentative_cost < g_cost.get(neighbor, float("inf")):
                g_cost[neighbor] = tentative_cost
                came_from[neighbor] = node
                estimated_total = tentative_cost + heuristic.get(neighbor, 0)
                heapq.heappush(
                    frontier,
                    (estimated_total, next(tie_breaker), neighbor),
                )

        if verbose:
            printable_frontier = [
                (node_name, score) for score, _, node_name in sorted(frontier)
            ]
            print(f"A* frontier (node, f): {printable_frontier}")
            print(f"A* visited: {sorted(expanded_cost)}")

    return None, None, expanded_count
