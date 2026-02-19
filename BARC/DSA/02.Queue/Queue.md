# QUEUE – Complete Guide
---

## 1. What is a Queue?

A **queue** is a **linear data structure** that follows the **FIFO (First In, First Out)** principle.  (The element inserted first is the first one to be removed.)

**Example**  
```
Enqueue 10 → [10]  
Enqueue 20 → [10, 20]  
Enqueue 30 → [10, 20, 30]  
Dequeue    → 10 (queue becomes [20, 30])  
Dequeue    → 20
```

**Formal Definition**  
A queue is an **abstract data type (ADT)** that supports two main operations:
- **Enqueue**: Insert an element at the **rear** (back).
- **Dequeue**: Remove and return the element from the **front**.

All insertions happen at one end (**rear**) and deletions from the other end (**front**). This enforces FIFO ordering.

---

## 2. Why Do We Need a Queue? (When to Use It)

We choose a queue when a problem naturally involves:
- **Ordered processing** – processing items in the order they arrive.
- **Fairness / Scheduling** – first come, first served.
- **Buffering** – handling data streams, asynchronous communication.
- **Breadth‑First Traversal** – exploring level by level.
- **Resource sharing** – managing requests to a shared resource (printer, CPU).

**Logical reasoning**  
If the earliest action must be processed first, **FIFO is optimal**, and queue is the natural choice.

---

## 3. Queue in Python – Implementations & Trade-offs

Python provides several ways to implement a queue.

### 3.1 Using List (Not Recommended for Performance)
```python
queue = []
queue.append(10)      # Enqueue – O(1) amortized
front = queue[0]      # Peek front – O(1)
queue.pop(0)          # Dequeue – O(n) – SLOW!
```
**Pros** – Simple.  
**Cons** – Dequeue is O(n) because all elements must shift left. **Never use list for queue in production/interviews.**

### 3.2 Using `collections.deque` (Recommended)
```python
from collections import deque
queue = deque()
queue.append(10)      # Enqueue – O(1)
queue.append(20)      # Enqueue – O(1)
front = queue[0]      # Peek front – O(1)
queue.popleft()       # Dequeue – O(1)
```
**Why?** `deque` (double-ended queue) is optimized for fast O(1) appends and pops from both ends.  
**Pros** – Fast O(1) enqueue/dequeue, simple syntax.  
**Cons** – Not thread-safe.

### 3.3 Using `queue.Queue` (Thread-Safe)
```python
from queue import Queue
q = Queue(maxsize=10)
q.put(10)             # Enqueue – block if full
item = q.get()        # Dequeue – block if empty
q.qsize()             # Approximate size
q.empty()             # Check if empty
q.full()              # Check if full
```
**Pros** – Thread‑safe, can set max size, supports timeouts.  
**Cons** – Slightly slower due to locking; not typical in algorithm interviews.

### 3.4 Using `multiprocessing.Queue` (Process-Safe)
```python
from multiprocessing import Queue
q = Queue()
q.put(10)             # Enqueue
item = q.get()        # Dequeue
```
**Pros** – Process‑safe for inter‑process communication.  
**Cons** – Overkill for single‑threaded algorithms.

### 3.5 Custom Queue Class (Linked List based)
```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value)
        if self.rear:
            self.rear.next = node
        self.rear = node
        if not self.front:
            self.front = node
        self.length += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        self.length -= 1
        return value

    def peek(self):
        if self.is_empty():
            return None
        return self.front.value

    def is_empty(self):
        return self.front is None

    def size(self):
        return self.length
```
**Pros** – No size limit, O(1) enqueue/dequeue.  
**Cons** – Extra memory per node, not cache‑friendly.

**Recommendation for interviews**  
- Use **`collections.deque`** for quick coding – it's the standard.  
- Mention `queue.Queue` if thread‑safety is required.  
- Implement custom linked‑list queue if asked to do so.

---

## 4. Basic Queue Operations & Complexity

| Operation    | Description                            | Time Complexity |
|--------------|----------------------------------------|-----------------|
| `enqueue(x)` | Insert x at rear                       | O(1)            |
| `dequeue()`  | Remove & return front element          | O(1)            |
| `peek()`     | Return front without removal           | O(1)            |
| `is_empty()` | Check if queue has no elements         | O(1)            |
| `size()`     | Number of elements                     | O(1) (if tracked) / O(n) |
| `is_full()`  | Only for bounded queues                | O(1)            |
| `search`     | Find element (not typical queue op)    | O(n)            |

**Space complexity** – O(n) for storing n elements.

---

## 5. Queue Variants

| Variant          | Description                                      | Use Case                          |
|------------------|--------------------------------------------------|-----------------------------------|
| **Simple Queue** | FIFO order                                       | Basic scheduling                  |
| **Circular Queue**| Rear wraps to front when full                   | Fixed-size buffer, memory efficiency |
| **Priority Queue**| Elements ordered by priority                    | Task scheduling, Dijkstra's algo |
| **Deque** (Double-Ended) | Insert/delete from both ends            | Sliding window, palindrome check |
| **Blocking Queue**| Blocks on put/get when full/empty              | Producer-consumer problems       |

---

## 6. Applications of Queue – Detailed

### 6.1 Process Scheduling (OS)
- **FIFO scheduling** – processes executed in order of arrival.
- **Round Robin** – each process gets a time slice, then goes to back of queue.

### 6.2 Breadth‑First Search (BFS)
- BFS on trees and graphs uses a queue to explore level by level.

### 6.3 Caching (FIFO Cache)
- When cache is full, the oldest entry is removed first.

### 6.4 Print Spooler
- Print jobs are queued and processed in order.

### 6.5 Asynchronous Data Transfer
- **I/O Buffers**, **pipe buffers** – data written and read in FIFO order.

### 6.6 Request Handling
- Web servers queue incoming requests.

### 6.7 Breadth‑First Traversal of Trees
- Level order traversal uses a queue.

### 6.8 Producer-Consumer Problem
- Queue buffers data between producer and consumer threads.

### 6.9 Keyboard Buffer
- Characters typed are stored in a queue until processed.

### 6.10 Call Center Systems
- Calls are handled in the order they arrive.

---

## 7. Implementation Types – In Depth

### 7.1 Array-based Queue (Static/Circular)
- Uses fixed-size array with `front` and `rear` pointers.
- **Enqueue**: `rear = (rear + 1) % capacity`, `arr[rear] = x`.
- **Dequeue**: `front = (front + 1) % capacity`, return old front.
- **Drawback**: Wasted space if not circular; overflow if full.

### 7.2 Dynamic Array Queue
- Resize when full; amortized O(1) enqueue.

### 7.3 Linked List Queue
- `front` points to head, `rear` points to tail.
- Enqueue at tail, dequeue at head – O(1).

**Comparison**

| Criteria        | Array (static) | Dynamic Array | Linked List   |
|-----------------|----------------|---------------|---------------|
| Memory          | Fixed          | May have wasted space | Extra per node |
| Access time     | O(1)           | O(1)          | O(1) (only ends)|
| Overflow        | Yes            | Rare (until memory full) | No            |
| Cache locality  | Good           | Good          | Poor          |
| Resize cost     | –              | Amortized O(1)| –             |

---

## 8. Queue Overflow & Underflow

- **Queue Overflow**  
  - Enqueuing onto a **full fixed‑size queue**.
- **Queue Underflow**  
  - Dequeuing from an **empty queue**.  
  - Should always check `is_empty()` before dequeue/peek.

---

## 9. Advantages of Queue

1. **Simple and intuitive** – easy to implement and reason about.
2. **Fair ordering** – processes data in arrival order.
3. **Fast operations** – enqueue/dequeue are O(1) with proper implementation.
4. **Natural fit** for scheduling, buffering, BFS.
5. **Decouples producers and consumers** – asynchronous processing.

---

## 10. Disadvantages of Queue

1. **Limited access** – only front and rear are directly accessible.
2. **No random access** – cannot access arbitrary element without dequeuing.
3. **Search is O(n)** – not designed for search.
4. **Fixed‑size issues** – static implementation may overflow or underutilize memory.
5. **Not cache‑friendly** (linked version) – nodes scattered in memory.

---

## 11. Important Interview Questions – Theory (80%)

These cover conceptual, design, and analytical questions.

### Basic Definitions & Properties
1. What is FIFO? Give a real‑life example.
2. How is queue different from stack? From array?
3. What are the primary queue operations? Their time complexities?
4. What is queue overflow? Queue underflow?
5. What is a circular queue? Why is it useful?
6. What is a double-ended queue (deque)?
7. Can you implement a queue using a stack? How many stacks are needed?
8. Can you implement a stack using a queue? Complexities?
9. What is a priority queue? How is it different from a simple queue?
10. What is a blocking queue? Where is it used?

### Implementation & Design
11. Compare array-based vs linked-list-based queue.
12. How would you implement a circular queue?
13. How to implement a queue that supports getMin()/getMax() in O(1)?
14. How to implement a queue using two stacks?
15. How to implement a stack using two queues?
16. How to design a thread-safe queue in Python?
17. What is the space complexity of BFS in terms of queue size?
18. How to implement a priority queue using a heap?
19. What is the difference between `collections.deque` and `queue.Queue`?
20. How to reverse a queue?

### Problem-Specific Concepts
21. How to implement a sliding window maximum using deque?
22. How to generate binary numbers from 1 to n using a queue?
23. How to implement a stack using queues with O(1) push?
24. How to find the first non-repeating character in a stream using queue?
25. How to implement a recent counter (number of requests in last 3000ms)?
26. How to check if a given tree is a complete binary tree using queue?
27. How to implement level order traversal of a binary tree?
28. How to connect nodes at the same level in a binary tree?
29. How to implement a queue with getMiddle() operation?
30. How to implement a queue that supports deletion of a given element?

### Advanced / Tricky
31. What happens in BFS when the graph is very wide?
32. How does queue help in solving the "rotten oranges" problem?
33. How to implement a queue with constant time operations for all functions?
34. What is the "producer-consumer" problem? How does queue solve it?
35. How to design a message queue system?
36. What is the difference between synchronous and asynchronous queues?
37. How to implement a queue with a circular buffer?
38. How to handle priority inversion in priority queues?
39. How to implement a deque with O(1) operations?
40. How to find the shortest path in an unweighted graph using BFS (queue)?

---

## 12. Important Interview Questions – Coding Concepts (20%)

These are not full coding problems but **solution patterns and logic** that you must be ready to explain/write quickly. Below are key implementations.

### 12.1 Queue using Two Stacks
```python
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []  # for enqueue
        self.stack2 = []  # for dequeue

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            raise IndexError("dequeue from empty queue")
        return self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1] if self.stack2 else None

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
```

### 12.2 Circular Queue (Array-based)
```python
class CircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, value: int) -> bool:
        if self.is_full():
            return False
        self.rear = (self.rear + 1) % self.k
        self.queue[self.rear] = value
        self.size += 1
        return True

    def dequeue(self) -> bool:
        if self.is_empty():
            return False
        self.front = (self.front + 1) % self.k
        self.size -= 1
        return True

    def front_value(self) -> Optional[int]:
        return None if self.is_empty() else self.queue[self.front]

    def rear_value(self) -> Optional[int]:
        return None if self.is_empty() else self.queue[self.rear]

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.k
```

### 12.3 Sliding Window Maximum (Monotonic Deque)
```python
from collections import deque

def max_sliding_window(nums, k):
    dq = deque()  # stores indices of elements in decreasing order
    result = []
    for i, num in enumerate(nums):
        # remove indices outside window
        while dq and dq[0] <= i - k:
            dq.popleft()
        # maintain decreasing order: remove smaller elements
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        # start recording when window is full
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result
```

### 12.4 Generate Binary Numbers from 1 to N
```python
from collections import deque

def generate_binary(n):
    result = []
    q = deque(['1'])
    for _ in range(n):
        front = q.popleft()
        result.append(front)
        q.append(front + '0')
        q.append(front + '1')
    return result
```

### 12.5 First Non-Repeating Character in Stream
```python
from collections import deque, defaultdict

def first_non_repeating(stream):
    dq = deque()
    count = defaultdict(int)
    result = []
    for ch in stream:
        count[ch] += 1
        dq.append(ch)
        while dq and count[dq[0]] > 1:
            dq.popleft()
        result.append(dq[0] if dq else '#')
    return result
```

### 12.6 Rotten Oranges (BFS with Queue)
```python
from collections import deque

def oranges_rotting(grid):
    rows, cols = len(grid), len(grid[0])
    fresh = 0
    queue = deque()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                fresh += 1
            elif grid[i][j] == 2:
                queue.append((i, j, 0))  # (row, col, time)
    if fresh == 0:
        return 0
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    max_time = 0
    while queue:
        i, j, time = queue.popleft()
        max_time = max(max_time, time)
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == 1:
                grid[ni][nj] = 2
                fresh -= 1
                queue.append((ni, nj, time + 1))
    return max_time if fresh == 0 else -1
```

### 12.7 Level Order Traversal of Binary Tree
```python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root):
    if not root:
        return []
    result = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.append(level)
    return result
```

### 12.8 Recent Counter (Number of Recent Calls)
```python
from collections import deque

class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)
```

### 12.9 Moving Average from Data Stream
```python
from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.total = 0

    def next(self, val: int) -> float:
        self.queue.append(val)
        self.total += val
        if len(self.queue) > self.size:
            self.total -= self.queue.popleft()
        return self.total / len(self.queue)
```

### 12.10 Stack using Two Queues
```python
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if not self.q1:
            raise IndexError("pop from empty stack")
        return self.q1.popleft()

    def top(self):
        return self.q1[0] if self.q1 else None

    def is_empty(self):
        return len(self.q1) == 0
```

---

## 13. Advanced Queue Patterns

### 13.1 Monotonic Queue (Deque)
A deque that maintains elements in **increasing** or **decreasing** order.  
**Use cases**: Sliding Window Maximum, Sliding Window Minimum.

**Template for decreasing deque (max)**
```python
from collections import deque

def monotonic_deque_template(nums):
    dq = deque()
    for i, num in enumerate(nums):
        # Remove elements that are out of consideration (e.g., out of window)
        while dq and condition_to_remove_from_front:
            dq.popleft()
        # Maintain order: remove from back if new element is greater (for max)
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        # Use dq[0] for current result
```

### 13.2 Priority Queue using `heapq`
```python
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def is_empty(self):
        return len(self.heap) == 0
```

---

## 14. Common Mistakes in Queue Interviews

1. **Not handling empty queue** – dequeuing without checking `is_empty()`.
2. **Using list for queue** – O(n) dequeue will be rejected.
3. **Confusing stack and queue order** – FIFO vs LIFO mix-up.
4. **Forgetting circular nature** – in circular queue, indices wrap around.
5. **Not resetting front/rear correctly** – when queue becomes empty.
6. **Ignoring thread‑safety** when required.
7. **BFS without visited set** – leads to infinite loops in graphs with cycles.
8. **Not considering deque for sliding window problems** – using list instead.

---

## 15. Queue in Python Standard Library – Summary

| Implementation        | Thread‑safe | Bounded | Typical Use                              |
|-----------------------|-------------|---------|------------------------------------------|
| `collections.deque`   | No          | No      | General purpose, fast O(1) operations   |
| `queue.Queue`         | Yes         | Yes     | Multi‑threaded producer-consumer         |
| `queue.PriorityQueue` | Yes         | Yes     | Thread‑safe priority queue               |
| `queue.LifoQueue`     | Yes         | Yes     | Thread‑safe stack (LIFO)                 |
| `multiprocessing.Queue`| Yes (process) | Yes  | Inter‑process communication              |
| `asyncio.Queue`       | Yes (async) | Yes     | Asynchronous programming                 |

---

## 16. Practice Problems – Categorized

**Easy**
- Implement Queue using Stacks
- Implement Stack using Queues
- Number of Recent Calls
- First Unique Character in a String
- Moving Average from Data Stream

**Medium**
- Sliding Window Maximum
- Design Circular Queue
- Generate Binary Numbers from 1 to N
- Rotten Oranges
- Binary Tree Level Order Traversal
- Connect Nodes at Same Level
- First Non-Repeating Character in Stream
- Task Scheduler

**Hard**
- Sliding Window Maximum (with deque)
- Shortest Path in Binary Matrix
- Minimum Knight Moves
- Design Hit Counter
- Find Median from Data Stream (with two heaps)
- Maximum of All Subarrays of Size K

---

## 17. Key Takeaways

- **FIFO** is the soul of queue. If your problem requires processing in arrival order, think queue.
- **Enqueue & Dequeue are O(1)** – with proper implementation (deque or linked list).
- **`collections.deque`** is the go‑to for interviews – know it well.
- **BFS** on trees/graphs relies on queues.
- **Monotonic deque** is a powerful optimization for sliding window problems.
- **Queue using two stacks** is a classic interview question.
- Always check edge cases: empty queue, single element, full bounded queue.
---
