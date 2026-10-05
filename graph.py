"""Sample weighted graph and heuristic for the search demonstrations."""

from typing import TypeAlias

Graph: TypeAlias = dict[str, dict[str, float]]


class WeightedGraph(dict[str, dict[str, float]]):
    """A weighted adjacency-list graph with a small edge helper."""

    def add_edge(self, source: str, target: str, weight: float) -> None:
        """Add a directed edge and ensure both endpoint nodes are present."""
        self.setdefault(source, {})[target] = weight
        self.setdefault(target, {})


# Edit these adjacency lists to match a graph from class. Edge weights must be
# non-negative for A* search.
GRAPH: Graph = WeightedGraph(
    {
        "S": {"A": 4, "B": 3},
        "A": {"G": 5},
        "B": {"G": 1},
        "G": {},
    }
)

# These estimates never exceed the actual remaining cost to G.
HEURISTIC: dict[str, float] = {
    "S": 4,
    "A": 5,
    "B": 1,
    "G": 0,
}
