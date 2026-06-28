# Depth-First Search (DFS) Traversal in Python

## Overview

This project demonstrates the **Depth-First Search (DFS)** traversal algorithm using a tree data structure in Python.

DFS is a graph and tree traversal technique that explores a node completely before moving to its sibling nodes. This implementation uses **recursion** to visit each node in a depth-first manner.

---

## Features

- Simple and beginner-friendly Python implementation
- Uses a custom `Node` class to represent a tree
- Recursive DFS traversal
- Prints nodes in Depth-First order
- Easy to understand and modify
- No external libraries required

---

## Algorithm

1. Start at the root node.
2. Visit the current node and print its value.
3. Recursively visit each child node from left to right.
4. Continue until all nodes have been visited.

---

## Project Structure

```
dfs-traversal/
│
├── dfs.py
└── README.md
```

---

## Tree Structure

```
        A
      / | \
     B  C  D
    / \ |   \
   E   F G   H
```

---

## Sample Output

```
DFS traversal of the tree:
A B E F C G D H
```

---

## Time Complexity

| Operation | Complexity |
|-----------|------------|
| DFS Traversal | O(n) |

Where:

- **n** = Total number of nodes in the tree

---

## Space Complexity

| Complexity |
|------------|
| O(h) |

Where:

- **h** = Height of the tree (due to the recursive call stack)
- In the worst case, the space complexity can be **O(n)** for a skewed tree.

---

## Applications

- Tree traversal
- Graph traversal
- Path finding
- Maze solving
- Topological sorting
- Artificial Intelligence search algorithms
- File system navigation

---

## How to Run

1. Clone the repository

```bash
git clone https://github.com/your-username/dfs-traversal.git
```

2. Navigate to the project folder

```bash
cd dfs-traversal
```

3. Run the Python file

```bash
python dfs.py
```

---

## Requirements

- Python 3.x

No external libraries are required.

---

## Learning Objectives

This project helps in understanding:

- Depth-First Search (DFS)
- Tree Data Structures
- Recursion
- Node-based Tree Implementation
- Tree Traversal Algorithms

---

## Author

**Jhansi**

---

## License

This project is open-source and available for educational purposes.
