"""Tests for the graph search algorithms."""

import subprocess
import sys
from pathlib import Path

from algorithms import a_star_search, breadth_first_search, depth_first_search
from graph import GRAPH, HEURISTIC, Graph

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def path_cost(graph: Graph, path: list[str]) -> float:
    """Return the sum of the edge weights along a path."""
    return sum(graph[source][target] for source, target in zip(path, path[1:]))


def is_valid_path(graph: Graph, path: list[str] | None, start: str, goal: str) -> bool:
    """Check that a path connects start to goal using real graph edges."""
    return (
        path is not None
        and path[0] == start
        and path[-1] == goal
        and all(
            target in graph.get(source, {})
            for source, target in zip(path, path[1:])
        )
    )


def test_bfs_finds_a_valid_path() -> None:
    path, expanded = breadth_first_search(GRAPH, "S", "G")

    assert is_valid_path(GRAPH, path, "S", "G")
    assert expanded > 0


def test_dfs_finds_a_valid_path() -> None:
    path, expanded = depth_first_search(GRAPH, "S", "G")

    assert is_valid_path(GRAPH, path, "S", "G")
    assert expanded > 0


def test_a_star_finds_the_lowest_cost_path() -> None:
    path, cost, expanded = a_star_search(GRAPH, "S", "G", HEURISTIC)

    assert is_valid_path(GRAPH, path, "S", "G")
    assert path is not None
    assert cost == path_cost(GRAPH, path) == 4
    assert path == ["S", "B", "G"]
    assert expanded > 0


def test_unreachable_goal_returns_none() -> None:
    graph: Graph = {"S": {"A": 1}, "A": {}, "G": {}}

    bfs_path, _ = breadth_first_search(graph, "S", "G")
    dfs_path, _ = depth_first_search(graph, "S", "G")
    astar_path, astar_cost, _ = a_star_search(
        graph, "S", "G", {"S": 0, "A": 0, "G": 0}
    )

    assert bfs_path is None
    assert dfs_path is None
    assert astar_path is None
    assert astar_cost is None


def test_each_algorithm_can_be_run_from_cli() -> None:
    for algo in ("bfs", "dfs", "astar"):
        result = subprocess.run(
            [sys.executable, "main.py", "--algo", algo, "--verbose"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        assert "Path found:" in result.stdout
        assert "Total cost:" in result.stdout
        assert "Nodes expanded:" in result.stdout
