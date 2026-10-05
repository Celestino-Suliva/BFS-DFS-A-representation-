# search-module

A beginner-friendly Python project demonstrating breadth-first search (BFS),
depth-first search (DFS), and A* search on a weighted graph represented as an
adjacency list. The sample graph and its admissible heuristic are in
[`graph.py`](graph.py), making it straightforward to change the graph to match
a class diagram.

## Requirements and setup

Python 3.10 or newer is recommended. From the project directory, optionally
create and activate a virtual environment, then install the test dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run the demo

```powershell
python main.py
python main.py --start S --goal G --verbose
python main.py --algo bfs --verbose
python main.py --algo dfs --verbose
python main.py --algo astar --verbose
```

`--algo` selects `bfs`, `dfs`, `astar`, or `all` (the default). Selecting one
algorithm prints its own step-by-step output and result summary; `all` prints
the comparison table. `--start` and `--goal` select nodes from the graph, and
`--verbose` prints each algorithm's expanded node and frontier at each step.
The demo reports the edge-cost total for each returned path. BFS and DFS do
not use edge weights to choose their paths, while A* does. Options can be
combined, for example `python main.py --algo astar --start S --goal G --verbose`.

Example output:

```text
Search comparison (S -> G)
Algorithm  Path found           Total cost   Nodes expanded
--------------------------------------------------------------
BFS        S -> A -> G          9            3
DFS        S -> A -> G          9            2
A*         S -> B -> G          4            2
```

## Algorithms

- **BFS** uses a FIFO queue (`collections.deque`) and explores by increasing
  number of edges. It is complete on a finite graph, but is not necessarily
  cost-optimal when edge weights differ.
- **DFS** uses an iterative LIFO stack and explores one branch deeply before
  backtracking. It is complete on a finite graph with visited-node tracking,
  but is not cost-optimal.
- **A\*** uses a min-heap (`heapq`) ordered by `f(n) = g(n) + h(n)`, where `g`
  is the cost so far and `h` estimates the remaining cost. With an admissible
  heuristic and non-negative edge weights, it is cost-optimal.

For the sample graph, `S -> A -> G` costs 9 and `S -> B -> G` costs 4. The
heuristic values in `graph.py` do not overestimate the true remaining cost to
`G`.

## Comparison

| Algorithm | Complete? | Optimal? | Time | Space |
|---|---|---|---|---|
| BFS | Yes, for a finite graph | Fewest edges; cost-optimal only with equal edge costs | O(V + E) | O(V) |
| DFS | Yes, for a finite graph with visited tracking | No | O(V + E) | O(V) |
| A* | Yes under the stated finite-graph and non-negative-cost assumptions | Yes with an admissible heuristic | Commonly O((V + E) log V) | O(V + E) |

Here `V` is the number of nodes and `E` is the number of edges. Actual A*
performance depends on the heuristic; an inconsistent heuristic can cause
nodes to be revisited.

## Tests

Install dependencies as above, then run:

```powershell
python -m pytest
```

The tests check that each algorithm returns a valid path, that A* returns the
lowest-cost route on the sample graph, and that an unreachable goal returns
`None`.

## Initialize and push a GitHub repository

Create an empty repository named `search-module` on GitHub first (do not
initialize it with a README, license, or .gitignore). Then run these commands
from this project directory, replacing `YOUR-USERNAME` with your GitHub
username:

```powershell
git init
git add README.md requirements.txt .gitignore main.py graph.py algorithms tests
git commit -m "Create BFS, DFS, and A* search demo"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/search-module.git
git push -u origin main
```

For later updates:

```powershell
git add .
git commit -m "Describe the change"
git push
```
