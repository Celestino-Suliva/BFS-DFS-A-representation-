"""Run BFS, DFS, and A* on the sample graph."""

import argparse

from algorithms import a_star_search, breadth_first_search, depth_first_search
from graph import GRAPH, HEURISTIC


def format_path(path: list[str] | None) -> str:
    """Format a path for display."""
    return " -> ".join(path) if path is not None else "No path found"


def path_cost(path: list[str] | None) -> int | float | None:
    """Return the total edge cost for a path, or None if there is no path."""
    if path is None:
        return None
    return sum(GRAPH[source][target] for source, target in zip(path, path[1:]))


def main() -> None:
    """Parse command-line options and print search results."""
    parser = argparse.ArgumentParser(
        description="Run BFS, DFS, and A* on a weighted graph."
    )
    parser.add_argument(
        "--algo", choices=("bfs", "dfs", "astar", "all"), default="all",
        help="algorithm to run (default: all)",
    )
    parser.add_argument("--start", default="S", help="starting node (default: S)")
    parser.add_argument("--goal", default="G", help="goal node (default: G)")
    parser.add_argument("--verbose", action="store_true", help="print each search step")
    args = parser.parse_args()

    if args.algo != "all":
        headings = {
            "bfs": "BFS (Breadth-First Search)",
            "dfs": "DFS (Depth-First Search)",
            "astar": "A* Search",
        }
        print(f"===== {headings[args.algo]} =====")
        if args.algo == "bfs":
            path, expanded = breadth_first_search(
                GRAPH, args.start, args.goal, verbose=args.verbose
            )
            cost = path_cost(path)
        elif args.algo == "dfs":
            path, expanded = depth_first_search(
                GRAPH, args.start, args.goal, verbose=args.verbose
            )
            cost = path_cost(path)
        else:
            path, cost, expanded = a_star_search(
                GRAPH, args.start, args.goal, HEURISTIC, verbose=args.verbose
            )
        print(f"Path found: {format_path(path)}")
        print(f"Total cost: {cost if cost is not None else 'N/A'}")
        print(f"Nodes expanded: {expanded}")
        return

    bfs_path, bfs_expanded = breadth_first_search(
        GRAPH, args.start, args.goal, verbose=args.verbose
    )
    dfs_path, dfs_expanded = depth_first_search(
        GRAPH, args.start, args.goal, verbose=args.verbose
    )
    astar_path, astar_cost, astar_expanded = a_star_search(
        GRAPH, args.start, args.goal, HEURISTIC, verbose=args.verbose
    )

    print(f"\nSearch comparison ({args.start} -> {args.goal})")
    print(f"{'Algorithm':<10} {'Path found':<20} {'Total cost':<12} Nodes expanded")
    print("-" * 62)
    rows = [
        ("BFS", bfs_path, path_cost(bfs_path), bfs_expanded),
        ("DFS", dfs_path, path_cost(dfs_path), dfs_expanded),
        ("A*", astar_path, astar_cost, astar_expanded),
    ]
    for name, path, cost, expanded in rows:
        cost_text = str(cost) if cost is not None else "N/A"
        print(f"{name:<10} {format_path(path):<20} {cost_text:<12} {expanded}")


if __name__ == "__main__":
    main()
