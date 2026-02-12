
---

# STACK – Comprehensive Guide

---

## 1. What is a Stack?

A **stack** is a **linear data structure** that follows the **LIFO (Last In, First Out)** principle.
The element inserted last is the first one to be removed.

### Example

```
Push 10 → [10]
Push 20 → [10, 20]
Push 30 → [10, 20, 30]
Pop → 30 (stack becomes [10, 20])
Pop → 20
```

### Formal Definition

A stack is an **abstract data type (ADT)** that supports two main operations:

* **Push**: Insert an element at the top.
* **Pop**: Remove and return the top element.

All insertions and deletions happen at **one end** called the **top**, enforcing LIFO ordering.

---

## 2. Why Do We Need a Stack?

Use a stack when a problem naturally involves:

* Reversal of order
* Nested structures such as parentheses or function calls
* Undo or redo operations
* Backtracking problems
* Expression evaluation

If the most recent action must be processed first, LIFO is the natural choice.

---

## 3. Stack in Python – Implementations and Trade-offs

Python does not have a dedicated Stack class, but several approaches exist.

### 3.1 Using List

```python
stack = []
stack.append(10)      # Push – O(1) amortized
top = stack[-1]       # Peek – O(1)
stack.pop()           # Pop – O(1)
empty = len(stack) == 0
```

**Pros**

* Simple
* Cache friendly
* O(1) amortized push and pop

**Cons**

* Not thread safe
* Occasional resizing cost

---

### 3.2 Using collections.deque

```python
from collections import deque

stack = deque()
stack.append(10)
stack.pop()
```

**Pros**

* O(1) operations
* Efficient for both ends

**Cons**

* Slightly more memory overhead

---

### 3.3 Using queue.LifoQueue

```python
from queue import LifoQueue

stack = LifoQueue(maxsize=10)
stack.put(10)
stack.get()
stack.qsize()
```

**Pros**

* Thread safe
* Supports size limits

**Cons**

* Slower due to locking overhead

---

### 3.4 Custom Stack Using Linked List

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.length += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        value = self.top.value
        self.top = self.top.next
        self.length -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.top.value

    def is_empty(self):
        return self.top is None
```

---

## 4. Basic Stack Operations and Complexity

| Operation  | Description                 | Time Complexity |
| ---------- | --------------------------- | --------------- |
| push(x)    | Insert element at top       | O(1)*           |
| pop()      | Remove and return top       | O(1)            |
| peek()     | Return top without removing | O(1)            |
| is_empty() | Check if empty              | O(1)            |
| size()     | Number of elements          | O(1) or O(n)    |
| search     | Find element                | O(n)            |

Space complexity: **O(n)**

---

## 5. Stack vs Other Linear Data Structures

| Feature | Stack | Queue | Deque     |
| ------- | ----- | ----- | --------- |
| Order   | LIFO  | FIFO  | Both      |
| Insert  | Top   | Rear  | Both ends |
| Delete  | Top   | Front | Both ends |

---

## 6. Applications of Stack

### Function Call Stack

Each function call creates a stack frame. Deep recursion can cause overflow.

### Recursion to Iteration

Recursive algorithms can be converted using an explicit stack.

### Syntax Validation

Balanced parentheses and tag validation.

### Expression Evaluation

Infix to postfix conversion and evaluation.

### Undo and Redo

Two stack approach.

### Browser Navigation

Back and forward stacks.

### Backtracking

DFS, maze solving, N Queens.

### Reversal Problems

Reverse string or linked list.

---

## 7. Implementation Types

### Static Array Based Stack

Fixed size, risk of overflow.

### Dynamic Array Stack

Resizes automatically, amortized O(1).

### Linked List Stack

No resizing, extra memory per node.

| Criteria       | Static Array | Dynamic Array | Linked List |
| -------------- | ------------ | ------------- | ----------- |
| Overflow       | Yes          | Rare          | No          |
| Memory         | Fixed        | Resizable     | Per node    |
| Cache locality | Good         | Good          | Poor        |

---

## 8. Stack Overflow and Underflow

**Stack Overflow**

* Fixed size stack full
* Too many recursive calls

**Stack Underflow**

* Pop on empty stack

Always check before popping.

---

## 9. Advantages

* Simple and intuitive
* O(1) operations
* Natural for recursive problems
* Controlled access

---

## 10. Disadvantages

* No random access
* Search is O(n)
* Static stack may overflow
* Linked list version not cache friendly

---

## 11. Stack Data Structure vs Memory Stack

| Data Structure Stack | Memory Stack            |
| -------------------- | ----------------------- |
| Abstract ADT         | OS managed memory       |
| Manual push and pop  | Automatic call handling |
| Used in programs     | Stores function frames  |

---

## 12. Interview Questions – Theory Focus

### Basic Concepts

* What is LIFO
* Difference between stack and queue
* Stack overflow and underflow
* Call stack and recursion
* Implement stack using queue
* Implement queue using stack
* Monotonic stack
* Stack vs heap memory

### Design Based

* Min stack in O(1)
* Two stacks in one array
* Stack with increment operation
* Reverse stack using recursion
* Sort stack using temporary stack
* Thread safe stack
* Amortized analysis of Python list

### Problem Specific

* Balanced parentheses
* Infix to postfix conversion
* Postfix evaluation
* Next greater element
* Stock span
* Largest rectangle in histogram
* Longest valid parentheses
* Browser history design

### Advanced

* Tail recursion optimization
* Stack frame components
* Stack unwinding
* Iterative vs recursive DFS
* Why stack cannot do BFS efficiently

---

## 13. Coding Patterns Overview

You should be able to quickly implement:

* Valid parentheses checker
* Min stack
* Next greater element
* Postfix evaluation
* Iterative DFS
* Largest rectangle logic

---

## 14. Advanced Stack Patterns

### Monotonic Stack

Used for next greater or smaller problems.

```python
stack = []
result = [0] * n

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        idx = stack.pop()
        result[idx] = i - idx
    stack.append(i)
```

---

### Stack with Min

Use auxiliary stack to store minimums.

---

### Iterative DFS

```python
def dfs_iterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                stack.append(neighbor)
```

---

## 15. Common Mistakes

* Not checking empty stack
* Using insert at index 0 instead of append
* Confusing heap and stack memory
* Ignoring recursion space complexity
* Off by one errors in monotonic stack

---

## 16. Python Stack Options Summary

| Implementation        | Thread Safe | Bounded | Use Case               |
| --------------------- | ----------- | ------- | ---------------------- |
| list                  | No          | No      | Interview coding       |
| deque                 | No          | No      | Efficient double ended |
| LifoQueue             | Yes         | Yes     | Multi-threaded         |
| multiprocessing.Queue | Yes         | Yes     | Inter process          |

---

## 17. Practice Problems

### Easy

* Valid Parentheses
* Min Stack
* Backspace String Compare
* Remove Adjacent Duplicates

### Medium

* Evaluate Reverse Polish Notation
* Next Greater Element
* Stock Span
* Decode String
* Simplify Path
* Iterative Tree Traversal

### Hard

* Largest Rectangle in Histogram
* Maximal Rectangle
* Trapping Rain Water
* Longest Valid Parentheses
* Basic Calculator

---

## 18. Key Takeaways

* LIFO defines stack behavior
* Push and pop are O(1)
* Python list is default choice
* Monotonic stack is powerful
* Recursion uses implicit stack
* Always handle edge cases
* Distinguish data structure stack and memory stack

---
