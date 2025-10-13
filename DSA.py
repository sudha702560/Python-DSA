"""
=====================================================================
🧠  DATA STRUCTURES & ALGORITHMS 
=====================================================================

Topics Covered:
---------------
1. Arrays vs Linked Lists
2. Stack vs Queue
3. Trees, Graphs, Heaps
4. Forests & Connected Components
5. Graph Types (DAG, Directed/Undirected, Weighted/Unweighted)
6. Binary Tree vs Binary Search Tree
7. Searching Algorithms
8. Graph Algorithms (Prim’s, Dijkstra’s, Kruskal’s, BFS, DFS)
9. Tree Traversals (Inorder, Preorder, Postorder, Level Order)
10. Sorting Algorithms (Merge Sort, Quick Sort)
11. Algorithm Paradigms (Divide & Conquer, Recursion, Greedy, DP)
12. Operators in Python (Arithmetic, Comparison, Logical, Bitwise)
13. Practice Functions (SumList, SumListEven, VowelCount, etc.)

=====================================================================
"""

# ===================================================================
# 🧩 OPERATORS IN PYTHON
# ===================================================================

# Arithmetic Operators
# +, -, *, /, //, %, +=, -=, *=, /=, //=
x = 10
x += 20   # x = x + 20
print("Arithmetic Example:", x)

# Comparison Operators: <, >, <=, >=, ==, !=
print("Comparison Example:", 5 > 3, 10 == 5)

# Logical Operators: AND, OR, NOT
print("AND Example:", True and False)
print("OR Example:", True or False)
print("NOT Example:", not True)

# Truthy and Falsy Values
# True → Any non-empty string, non-zero number, True
# False → Empty string, 0, False

# Bitwise Operators: AND (&), OR (|), XOR (^), NOT (~), <<, >>
a = 5  # 101
b = 6  # 110
print("Bitwise AND:", a & b)   # 100 = 4
print("Bitwise OR:", a | b)    # 111 = 7
print("Bitwise XOR:", a ^ b)   # 011 = 3

# Left and Right Shift
n = 5
print("Left Shift (n << 2):", n << 2)   # 5 * 2^2 = 20
print("Right Shift (n >> 1):", n >> 1)  # 5 / 2^1 = 2

# Operator Precedence
print("3 + 4 * 5 =", 3 + 4 * 5)         # 23
print("(3 + 4) * 5 =", (3 + 4) * 5)     # 35

# ===================================================================
# 🔁 BASIC PYTHON FUNCTIONS
# ===================================================================

def PrintList(li):
    """Print all elements in a list."""
    for i in li:
        print(i, end=" ")
    print()  # newline

li2 = [12, 34, 56, 78, 90]
PrintList(li2)


# Simple Function
def Add():
    """Add two fixed numbers."""
    x = 20
    y = 70
    print("Sum:", x + y)

Add()


# Function with Parameters
def AddXY(x, y):
    """Add two numbers provided as parameters."""
    print("Sum:", x + y)

AddXY(20, 40)
AddXY(120, 40)


# Function with Return
def AddReturn(x, y):
    """Return the sum of two numbers."""
    return x + y

print("Returned Sum:", AddReturn(20, 40))

# ===================================================================
# 🧮 LIST PROCESSING EXAMPLES
# ===================================================================

def SumList(li):
    """Return the sum of all elements in a list."""
    result = 0
    for i in li:
        result += i
    return result

li2 = [11, 35, 5, 78, 90]
print("Sum of List:", SumList(li2))


def SumListEven(li):
    """Return the sum of even numbers in a list."""
    result = 0
    for i in li:
        if i % 2 == 0:
            result += i
    return result

li2 = [11, 35, 5, 78, 90]
print("Sum of Even Numbers:", SumListEven(li2))


def CountEven(li):
    """Count how many even numbers are in the list."""
    result = 0
    for i in li:
        if i % 2 == 0:
            result += 1
    return result

print("Count of Even Numbers:", CountEven(li2))

# ===================================================================
# 🔤 STRING PROCESSING
# ===================================================================

def VowelCount(s):
    """Count how many vowels are in a string."""
    result = 0
    s = s.lower()
    vowels = "aeiou"
    for ch in s:
        if ch in vowels:
            result += 1
    return result

s = "ThIsIsPythonclass"
print("Vowel Count:", VowelCount(s))


def CharFrequency(s):
    """Return frequency of each character in a string."""
    freq = {}
    for ch in s.lower():
        freq[ch] = freq.get(ch, 0) + 1
    return freq

s = "HelloWorld"
print("Character Frequencies:", CharFrequency(s))

# ===================================================================
# 🔢 NUMBER OPERATIONS
# ===================================================================

# Counting digits, product, and sum of digits
def DigitOperations(n):
    """Return count, sum, and product of digits in a number."""
    count = 0
    sum_digits = 0
    product = 1

    while n != 0:
        temp = n % 10
        n = n // 10
        count += 1
        sum_digits += temp
        product *= temp

    return count, sum_digits, product

n = 123434
count, s, p = DigitOperations(n)
print(f"Number: {n} | Digits: {count}, Sum: {s}, Product: {p}")

# Even digit count
def EvenDigitCount(n):
    """Count even digits in a number."""
    count = 0
    while n != 0:
        temp = n % 10
        n = n // 10
        if temp % 2 == 0:
            count += 1
    return count

print("Even Digit Count:", EvenDigitCount(123434))

# ===================================================================
# 🧠 THEORETICAL SECTION (NOT CODED)
# ===================================================================
"""
ARRAY vs LINKED LIST:
---------------------
Array:  Contiguous memory, fixed size, random access O(1)
Linked List: Dynamic size, non-contiguous, sequential access O(n)

STACK vs QUEUE:
---------------
Stack: LIFO (push, pop)
Queue: FIFO (enqueue, dequeue)

TREE:
-----
Hierarchical structure with nodes (root, child, leaf)

GRAPH:
------
Set of vertices (nodes) and edges (connections)

HEAP:
-----
Binary tree satisfying heap property (min/max)

FOREST:
-------
Collection of disjoint trees.

CONNECTED COMPONENTS:
---------------------
Subgraphs in which all vertices are connected.

GRAPH TYPES:
------------
Directed vs Undirected
Weighted vs Unweighted
DAG = Directed Acyclic Graph (no cycles)

BINARY TREE vs BINARY SEARCH TREE:
----------------------------------
Binary Tree: Each node has ≤ 2 children.
BST: Left < Root < Right ordering property.

TREE TRAVERSALS:
----------------
Inorder   → Left → Root → Right
Preorder  → Root → Left → Right
Postorder → Left → Right → Root
Level Order → BFS Traversal

SEARCH ALGORITHMS:
------------------
Linear Search: O(n)
Binary Search: O(log n)

GRAPH ALGORITHMS:
-----------------
BFS (Breadth First Search)
DFS (Depth First Search)
Prim’s, Kruskal’s, Dijkstra’s (Shortest Path / MST)

SORTING ALGORITHMS:
-------------------
Merge Sort  → O(n log n), Stable, Not In-place
Quick Sort  → O(n log n), Unstable, In-place

ALGORITHM DESIGN PARADIGMS:
---------------------------
Divide & Conquer, Recursion, Greedy, Dynamic Programming
"""

# ===================================================================
# 🧮 PSEUDOCODES (EXAMPLES)
# ===================================================================
"""
MERGE SORT (Divide & Conquer):
------------------------------
MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        MergeSort(left)
        MergeSort(right)
        merge(left, right, arr)

QUICK SORT:
-----------
QuickSort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        QuickSort(arr, low, p-1)
        QuickSort(arr, p+1, high)

BINARY SEARCH:
--------------
BinarySearch(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
"""
