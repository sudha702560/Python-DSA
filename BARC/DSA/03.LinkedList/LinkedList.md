# LINKED LIST – Complete Guide

## 1. What is a Linked List?

A **linked list** is a **linear data structure** where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked list elements are not stored in contiguous memory locations.

**Node Structure**  
Each node contains:
- **Data** – the actual value.
- **Next** – a reference (pointer) to the next node.

**Example**  
```
[10 | next] --> [20 | next] --> [30 | next] --> None
```

---

## 2. Why Do We Need a Linked List?

Linked lists are used when:
- **Dynamic size** is required (unlike fixed-size arrays).
- **Frequent insertions/deletions** at arbitrary positions are needed.
- **Memory is fragmented** and contiguous allocation is not possible.
- Implementing other data structures like stacks, queues, graphs.

**Logical reasoning**  
If you need efficient insertions/deletions (O(1) at head) and don't require random access, a linked list is a natural choice.

---

## 3. Types of Linked Lists

| Type                | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| **Singly Linked List** | Each node points to the next node only.                         |
| **Doubly Linked List** | Each node has pointers to both next and previous.               |
| **Circular Linked List** | Last node points back to the first node (can be singly or doubly). |

---

## 4. Linked List in Python – Implementations

### 4.1 Singly Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete_node(self, key):
        curr = self.head
        if curr and curr.data == key:
            self.head = curr.next
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next

    def search(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return True
            curr = curr.next
        return False

    def display(self):
        elements = []
        curr = self.head
        while curr:
            elements.append(curr.data)
            curr = curr.next
        print(" -> ".join(map(str, elements)))
```

### 4.2 Doubly Linked List
```python
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = DNode(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_node(self, key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if curr:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                self.head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
```

### 4.3 Circular Linked List
```python
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = new_node
        new_node.next = self.head
        self.head = new_node

    def display(self):
        if not self.head:
            return
        elements = []
        curr = self.head
        while True:
            elements.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        print(" -> ".join(map(str, elements)) + " -> (back to head)")
```

---

## 5. Basic Operations & Complexity

| Operation               | Singly Linked List | Doubly Linked List |
|-------------------------|--------------------|--------------------|
| Insert at head          | O(1)               | O(1)               |
| Insert at tail          | O(n)               | O(1) if tail pointer, else O(n) |
| Insert at given position| O(n)               | O(n)               |
| Delete at head          | O(1)               | O(1)               |
| Delete at tail          | O(n)               | O(1) if tail pointer, else O(n) |
| Delete by value         | O(n)               | O(n)               |
| Search                  | O(n)               | O(n)               |
| Access (index)          | O(n)               | O(n)               |

**Space complexity** – O(n) for storing n nodes.

---

## 6. Advantages of Linked List

1. **Dynamic size** – grows and shrinks at runtime.
2. **Efficient insertions/deletions** – at beginning in O(1).
3. **No memory wastage** – memory allocated per node as needed.
4. **Implementation of other data structures** – stacks, queues, graphs, etc.
5. **Easy to merge/split** lists.

---

## 7. Disadvantages of Linked List

1. **No random access** – must traverse from head.
2. **Extra memory** – for storing pointers.
3. **Not cache‑friendly** – nodes may be scattered in memory.
4. **Reverse traversal is costly** (singly) – O(n) to reach previous node.
5. **Complex implementation** – especially doubly and circular.

---

## 8. Applications of Linked List

- **Implementation of stacks and queues**
- **Graph adjacency lists**
- **Music player playlists** (circular)
- **Undo/redo functionality** (doubly)
- **Memory management** (free lists)
- **Polynomial arithmetic**
- **Hash table chaining**
- **Dynamic memory allocation**

---

## 9. Important Interview Questions

These cover conceptual, design, and analytical questions.

### Basic Definitions & Properties
1. What is a linked list? How is it different from an array?
2. Explain the structure of a singly linked list node.
3. What are the advantages and disadvantages of linked lists over arrays?
4. What is a doubly linked list? When would you use it?
5. What is a circular linked list? Give a real‑life example.
6. How do you traverse a linked list?
7. How do you insert a node at the beginning, end, and middle of a singly linked list?
8. How do you delete a node from a singly linked list given only the node pointer?
9. How do you reverse a singly linked list (iterative and recursive)?
10. How do you detect a cycle in a linked list? (Floyd’s cycle detection)

### Implementation & Design
11. Compare singly, doubly, and circular linked lists.
12. How would you implement a stack using a linked list?
13. How would you implement a queue using a linked list?
14. How do you find the middle of a linked list in one pass?
15. How do you find the nth node from the end of a linked list?
16. How do you merge two sorted linked lists?
17. How do you check if two linked lists intersect? Find intersection point.
18. How do you remove duplicates from an unsorted linked list?
19. How do you split a circular linked list into two halves?
20. How do you add two numbers represented by linked lists?

### Problem-Specific Concepts
21. What is Floyd’s cycle detection algorithm? How does it work?
22. How do you find the starting node of a cycle in a linked list?
23. How do you reverse a linked list in groups of size k?
24. How do you check if a linked list is a palindrome?
25. How do you rotate a linked list to the right by k places?
26. How do you rearrange a linked list in place (e.g., odd-even list)?
27. How do you clone a linked list with random pointers?
28. How do you sort a linked list? (Merge sort preferred)
29. How do you flatten a multilevel doubly linked list?
30. How do you subtract two numbers represented by linked lists?

### Advanced / Tricky
31. Explain the concept of a skip list. How is it related to linked lists?
32. What is the XOR linked list? How does it save memory?
33. How do you implement an LRU cache using a doubly linked list and hash map?
34. How do you find the length of a cycle in a linked list?
35. How do you pairwise swap nodes in a linked list?
36. How do you segregate even and odd nodes in a linked list?
37. How do you delete nodes which have a greater value on the right?
38. How do you sort a linked list of 0s, 1s, and 2s?
39. How do you reverse a doubly linked list?
40. How do you convert a binary tree to a doubly linked list (in‑place)?

---

## 10. Important Interview Questions – Coding Patterns (20%)

These are solution patterns you must be ready to write/explain.

### 10.1 Reverse a Singly Linked List (Iterative)
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

### 10.2 Detect Cycle (Floyd’s Algorithm)
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

### 10.3 Find Middle Node
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

### 10.4 Merge Two Sorted Lists
```python
def merge_sorted(l1, l2):
    dummy = Node(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
```

### 10.5 Remove Nth Node from End
```python
def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = dummy
    second = dummy
    for _ in range(n + 1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next
```

### 10.6 Add Two Numbers (represented as lists)
```python
def add_two_numbers(l1, l2):
    dummy = Node(0)
    curr = dummy
    carry = 0
    while l1 or l2 or carry:
        v1 = l1.data if l1 else 0
        v2 = l2.data if l2 else 0
        total = v1 + v2 + carry
        carry = total // 10
        curr.next = Node(total % 10)
        curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return dummy.next
```

### 10.7 Check Palindrome
```python
def is_palindrome(head):
    # Find middle, reverse second half, compare
    if not head or not head.next:
        return True
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # reverse from slow
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    # compare
    left, right = head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next
    return True
```

### 10.8 Intersection of Two Lists
```python
def get_intersection_node(headA, headB):
    a, b = headA, headB
    while a != b:
        a = a.next if a else headB
        b = b.next if b else headA
    return a
```

### 10.9 Clone List with Random Pointer
```python
def copy_random_list(head):
    if not head:
        return None
    # Insert copy nodes after each original
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next
    # Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next
    # Separate lists
    dummy = Node(0)
    copy = dummy
    curr = head
    while curr:
        copy.next = curr.next
        curr.next = curr.next.next
        copy = copy.next
        curr = curr.next
    return dummy.next
```

### 10.10 Reverse in Groups of K
```python
def reverse_k_group(head, k):
    if not head or k == 1:
        return head
    dummy = Node(0)
    dummy.next = head
    prev = dummy
    while True:
        # Check if there are k nodes left
        test = prev
        for _ in range(k):
            test = test.next
            if not test:
                return dummy.next
        # Reverse k nodes
        curr = prev.next
        next_node = None
        for _ in range(k - 1):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        prev = curr
```

---

## 11. Common Mistakes in Linked List Interviews

1. **Losing reference to head** – forgetting to update head when inserting/deleting.
2. **Not handling edge cases** – empty list, single node, two nodes.
3. **Infinite loops** – in cycle detection or traversal without termination.
4. **Dereferencing null** – accessing `node.next` when node is None.
5. **Forgetting to update `prev` pointers** in doubly linked list operations.
6. **Off-by-one errors** in length calculations or k-group reversal.
7. **Not using dummy nodes** when head may change.
8. **Confusing iteration vs. recursion** – recursion depth for long lists.

---

## 12. Linked List in Python Standard Library

Python does not have a built-in linked list, but `collections.deque` is implemented as a doubly linked list internally. For custom needs, you implement as shown.

---

## 13. Practice Problems – Categorized

**Easy**
- Reverse a Linked List
- Middle of the Linked List
- Detect Cycle in Linked List
- Merge Two Sorted Lists
- Remove Duplicates from Sorted List
- Intersection of Two Linked Lists
- Palindrome Linked List
- Remove Linked List Elements

**Medium**
- Add Two Numbers (represented as lists)
- Copy List with Random Pointer
- Sort List (merge sort)
- Reorder List
- Odd Even Linked List
- Linked List Cycle II (find cycle start)
- Remove Nth Node From End
- Rotate List
- Partition List
- Swap Nodes in Pairs

**Hard**
- Reverse Nodes in k-Group
- Merge k Sorted Lists
- LRU Cache (using doubly linked list + hashmap)
- Flatten a Multilevel Doubly Linked List
- Insertion Sort List
- Convert Sorted List to Binary Search Tree

---

## 14. Key Takeaways

- **Linked lists excel at insertions/deletions** but lack random access.
- **Always handle edge cases** (empty list, single node) explicitly.
- **Use dummy nodes** to simplify head modifications.
- **Floyd’s cycle detection** is a must‑know pattern.
- **Two‑pointer techniques** (slow/fast) solve many problems (middle, cycle, nth from end).
- **Recursive solutions** can be elegant but risk stack overflow for long lists.
- **Practice pointer manipulations** until they become second nature.

---