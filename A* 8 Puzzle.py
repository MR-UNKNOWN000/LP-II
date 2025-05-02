Here's a detailed **explanation**, **algorithm**, and **oral Q\&A** for your Python program that solves the **8-puzzle problem** using a **Greedy Best-First Search (heuristic-based)** strategy:

---

### 🔍 **What is the 8 Puzzle Problem?**

The **8-puzzle problem** is a classic AI problem involving a 3x3 grid with 8 numbered tiles and one empty space (`-1` in your code). The goal is to **reach a target configuration** by sliding the tiles into the empty space using the **fewest moves** possible.

---

### ✅ **Summary of Your Program**

* Uses a **Greedy approach with a heuristic** (Manhattan Distance).
* Moves the empty tile based on the **minimum heuristic cost**.
* Keeps track of moves using a global variable `g`.

---

### 🧠 Heuristic Used

```python
h += (abs(j - i)) // 3 + (abs(j - i)) % 3
```

This computes the **Manhattan Distance** for each tile, summing:

* Vertical distance: `abs(j - i) // 3`
* Horizontal distance: `abs(j - i) % 3`

---

### ⚙️ Algorithm Explanation (Step-by-Step)

#### ✅ Step 1: Input the Start and Goal State

* User enters 9 numbers for each.
* `-1` represents the empty tile.

#### ✅ Step 2: Solvability Check

* Count **inversions** (i.e., number of larger tiles before a smaller one).
* If number of inversions is even → the puzzle is solvable.

#### ✅ Step 3: Heuristic Evaluation

* For each move, compute total cost `f = h + g`.
* `h` is heuristic (distance), `g` is the depth (number of moves so far).

#### ✅ Step 4: Move Generation

* From the current state, generate up to 4 possible moves:

  * Move left, right, up, down (if within bounds).
* Select the one with the **minimum `f` value** and proceed.

#### ✅ Step 5: Recursive Solve

* Repeat the process recursively until heuristic `f == g` (i.e., h = 0, goal reached).

---

### ✅ Sample Input & Output

#### Example:

```
Start:  3 7 6 5 1 2 4 -1 8
Goal:   5 3 6 7 -1 2 4 1 8
```

Output:

```
Initial board:
3 7 6
5 1 2
4 _ 8

Next steps with boards...
Solved in X moves
```

---

### 📘 Q\&A for Viva / Oral Exams

---

#### 💬 **Q1: What algorithm is used here?**

**A:** A heuristic-based Greedy Best-First Search is used. It selects the move with the lowest heuristic (Manhattan distance) plus cost `g`.

---

#### 💬 **Q2: What is the purpose of the `heuristic` function?**

**A:** It calculates the estimated cost (`h`) to reach the goal from the current state using Manhattan Distance, added to the current move count `g`.

---

#### 💬 **Q3: Why do we use the `solvable()` function?**

**A:** To check if the initial state can be solved by counting **inversions**. Only configurations with even inversions are solvable in the 8-puzzle.

---

#### 💬 **Q4: Why is Manhattan Distance used as a heuristic?**

**A:** Because it gives an admissible and consistent estimate of the distance each tile is from its goal position, leading to efficient and accurate search.

---

#### 💬 **Q5: What are the limitations of this approach?**

**A:**

* It does not avoid **repeated states**, so it might loop or repeat.
* It lacks **backtracking** or proper state tracking (no visited states).
* Might not find the **optimal path** in all cases.

---

#### 💬 **Q6: What happens if multiple moves have the same heuristic?**

**A:** The code checks in order: left, right, down, up — and picks the first with minimum `f`. This may lead to suboptimal paths.

---

#### 💬 **Q7: What does the `g` variable track?**

**A:** It tracks the **depth** or the number of moves made so far.

---

#### 💬 **Q8: Can this be improved with A*?*\*

**A:** Yes. If you add proper state tracking (visited set) and priority queue (min-heap), and allow backtracking, it becomes A\* search.

---
