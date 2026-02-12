"""
================================================================================
            STACK DATA STRUCTURE – 40 COMPREHENSIVE MCQs
================================================================================
"""

def main():
    # ==============================================================================
    # QUESTION 1
    # ==============================================================================
    print("1. What does LIFO stand for in the context of a stack?")
    print("# A) Last In, First Out")
    print("# B) Last In, Fast Out")
    print("# C) Long In, First Out")
    print("# D) Linear Input, Fixed Output")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 2
    # ==============================================================================
    print("2. Which of the following is NOT a basic stack operation?")
    print("# A) push")
    print("# B) pop")
    print("# C) peek")
    print("# D) enqueue")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 3
    # ==============================================================================
    print("3. What is the time complexity of a `pop()` operation in a stack implemented using a Python list?")
    print("# A) O(1)")
    print("# B) O(n)")
    print("# C) O(log n)")
    print("# D) O(n²)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 4
    # ==============================================================================
    print("4. Which Python module provides a thread‑safe stack implementation?")
    print("# A) collections.deque")
    print("# B) queue.LifoQueue")
    print("# C) array.array")
    print("# D) threading.Stack")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 5
    # ==============================================================================
    print("5. A stack is a ______ data structure.")
    print("# A) linear")
    print("# B) non-linear")
    print("# C) hierarchical")
    print("# D) graph-based")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 6
    # ==============================================================================
    print("6. Which of the following is a real‑life example of a stack?")
    print("# A) Printer queue")
    print("# B) Waiting line at a ticket counter")
    print("# C) Undo operation in a text editor")
    print("# D) Round‑robin scheduling")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 7
    # ==============================================================================
    print("7. What will be the output if we perform `pop()` on an empty stack using a typical linked‑list implementation?")
    print("# A) None")
    print("# B) 0")
    print("# C) IndexError / Underflow exception")
    print("# D) -1")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 8
    # ==============================================================================
    print("8. Which of the following is **not** an application of stack?")
    print("# A) Function call management")
    print("# B) Parsing expressions")
    print("# C) Breadth‑First Search")
    print("# D) Undo/Redo")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 9
    # ==============================================================================
    print("9. In a monotonic increasing stack, the elements are stored in:")
    print("# A) Strictly increasing order from bottom to top")
    print("# B) Strictly decreasing order from bottom to top")
    print("# C) Any order")
    print("# D) Non‑increasing order")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 10
    # ==============================================================================
    print("10. What is the best auxiliary space complexity for a Min Stack that supports `getMin()` in O(1) time?")
    print("# A) O(1)")
    print("# B) O(n)")
    print("# C) O(log n)")
    print("# D) O(n²)")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 11
    # ==============================================================================
    print("11. Which of the following problems is **not** typically solved using a stack?")
    print("# A) Next Greater Element")
    print("# B) Valid Parentheses")
    print("# C) Finding shortest path in unweighted graph")
    print("# D) Stock Span")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 12
    # ==============================================================================
    print("12. The call stack is a region of:")
    print("# A) Heap memory")
    print("# B) Stack memory")
    print("# C) Data segment")
    print("# D) Code segment")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 13
    # ==============================================================================
    print("13. What is the output of the following code snippet?")
    print("# stack = []")
    print("# stack.append(1)")
    print("# stack.append(2)")
    print("# stack.append(3)")
    print("# print(stack.pop())")
    print("# print(stack[-1])")
    print("# A) 3, 2")
    print("# B) 2, 3")
    print("# C) 3, 1")
    print("# D) 1, 2")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 14
    # ==============================================================================
    print("14. Which of the following is true about a stack implemented with a singly linked list?")
    print("# A) Push operation is O(n)")
    print("# B) Pop operation is O(n)")
    print("# C) Both push and pop are O(1)")
    print("# D) Peek operation is O(n)")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 15
    # ==============================================================================
    print("15. How many stacks are required to implement a queue efficiently?")
    print("# A) One")
    print("# B) Two")
    print("# C) Three")
    print("# D) None")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 16
    # ==============================================================================
    print("16. In a static array‑based stack, the condition for **overflow** is:")
    print("# A) top == -1")
    print("# B) top == capacity - 1")
    print("# C) top == 0")
    print("# D) top == capacity")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 17
    # ==============================================================================
    print("17. The postfix expression `3 4 + 2 *` evaluates to:")
    print("# A) 14")
    print("# B) 10")
    print("# C) 7")
    print("# D) 12")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 18
    # ==============================================================================
    print("18. Which data structure is used during recursion by the compiler?")
    print("# A) Queue")
    print("# B) Stack")
    print("# C) Tree")
    print("# D) Graph")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 19
    # ==============================================================================
    print("19. What does the `peek()` operation return?")
    print("# A) The top element and removes it")
    print("# B) The top element without removing it")
    print("# C) The bottom element")
    print("# D) The size of the stack")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 20
    # ==============================================================================
    print("20. Which of the following is **not** an advantage of a linked list over an array for stack implementation?")
    print("# A) Dynamic size")
    print("# B) No overflow until heap memory exhausted")
    print("# C) Better cache locality")
    print("# D) Easier to expand")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 21
    # ==============================================================================
    print("21. What is the minimum number of stacks needed to implement a function that returns the minimum element in O(1) time?")
    print("# A) 0")
    print("# B) 1")
    print("# C) 2")
    print("# D) 3")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 22
    # ==============================================================================
    print("22. If characters are pushed onto a stack in order: `A`, `B`, `C`, `D`, then popped and printed, what is the output?")
    print("# A) A B C D")
    print("# B) D C B A")
    print("# C) D A B C")
    print("# D) A D C B")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 23
    # ==============================================================================
    print("23. Which algorithm uses a stack for its iterative implementation?")
    print("# A) Breadth‑First Search")
    print("# B) Depth‑First Search")
    print("# C) Prim’s algorithm (basic)")
    print("# D) Dijkstra’s algorithm")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 24
    # ==============================================================================
    print("24. What is the time complexity of finding the next greater element for all elements in an array using a monotonic stack?")
    print("# A) O(n)")
    print("# B) O(n²)")
    print("# C) O(n log n)")
    print("# D) O(log n)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 25
    # ==============================================================================
    print("25. In a balanced parentheses problem, what is pushed onto the stack when an opening bracket is encountered?")
    print("# A) The corresponding closing bracket")
    print("# B) The opening bracket itself")
    print("# C) The index of the bracket")
    print("# D) Nothing is pushed")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 26
    # ==============================================================================
    print("26. Which of the following is an example of a **prefix** expression?")
    print("# A) + A B")
    print("# B) A B +")
    print("# C) A + B")
    print("# D) (A + B)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 27
    # ==============================================================================
    print("27. The maximum number of parentheses pairs that can be stored in a stack of size `S` is:")
    print("# A) S/2")
    print("# B) S")
    print("# C) 2S")
    print("# D) S²")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 28
    # ==============================================================================
    print("28. Which of the following statements is **false**?")
    print("# A) Stack can be implemented using an array")
    print("# B) Stack can be implemented using a linked list")
    print("# C) Stack is a restricted data structure")
    print("# D) Stack supports random access")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 29
    # ==============================================================================
    print("29. What is the result of evaluating the postfix expression `5 6 2 + * 4 /`?")
    print("# A) 10")
    print("# B) 8")
    print("# C) 6")
    print("# D) 12")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 30
    # ==============================================================================
    print("30. In which of the following scenarios is stack **not** suitable?")
    print("# A) Reversing a string")
    print("# B) Checking for palindrome")
    print("# C) Level‑order traversal of a tree")
    print("# D) Evaluating postfix")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 31
    # ==============================================================================
    print("31. If the sequence of operations is: `push(1)`, `push(2)`, `pop()`, `push(3)`, `pop()`, `pop()`. What is the sequence of popped values?")
    print("# A) 2, 3, 1")
    print("# B) 2, 1, 3")
    print("# C) 1, 2, 3")
    print("# D) 3, 2, 1")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 32
    # ==============================================================================
    print("32. A stack is said to be in **underflow** condition when:")
    print("# A) We try to push when the stack is full")
    print("# B) We try to pop when the stack is empty")
    print("# C) The stack contains an odd number of elements")
    print("# D) The top pointer is at the middle")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 33
    # ==============================================================================
    print("33. Which of the following is **not** a property of a stack?")
    print("# A) Homogeneous elements")
    print("# B) Dynamic size (usually)")
    print("# C) FIFO access")
    print("# D) LIFO access")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 34
    # ==============================================================================
    print("34. The minimum number of stacks required to implement a **queue** is:")
    print("# A) 1")
    print("# B) 2")
    print("# C) 3")
    print("# D) 4")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 35
    # ==============================================================================
    print("35. Which operation is O(1) in `collections.deque` but O(n) in a Python list?")
    print("# A) pop() (from right)")
    print("# B) append()")
    print("# C) popleft()")
    print("# D) insert(0, x)")
    print("Answer: C")
    print("# Note: insert(0, x) is O(n) in both list and deque; popleft() is O(1) in deque but not available in list.")
    print()

    # ==============================================================================
    # QUESTION 36
    # ==============================================================================
    print("36. Which of the following correctly represents an infix to postfix conversion using stack?")
    print("# A) Operands are pushed onto stack")
    print("# B) Operators are pushed onto stack and popped based on precedence")
    print("# C) Both operands and operators are pushed")
    print("# D) Only parentheses are pushed")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 37
    # ==============================================================================
    print("37. How many times is the stack popped while evaluating the postfix expression `2 3 4 * + 5 -`?")
    print("# A) 3")
    print("# B) 4")
    print("# C) 5")
    print("# D) 6")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 38
    # ==============================================================================
    print("38. Which of the following is **true** about the memory stack?")
    print("# A) It is shared among all threads")
    print("# B) It grows upwards")
    print("# C) It stores dynamically allocated objects")
    print("# D) Each function call creates a stack frame")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 39
    # ==============================================================================
    print("39. What is the output of the following?")
    print("# def f(x):")
    print("#     if x == 0:")
    print("#         return 0")
    print("#     return x + f(x-1)")
    print("# print(f(3))")
    print("# Without tail‑call optimization, how many stack frames are created?")
    print("# A) 3")
    print("# B) 4")
    print("# C) 5")
    print("# D) 6")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 40
    # ==============================================================================
    print("40. Which of the following problems uses the concept of a **monotonic stack**?")
    print("# A) Binary search")
    print("# B) Largest rectangle in histogram")
    print("# C) Merge sort")
    print("# D) Knuth‑Morris‑Pratt algorithm")
    print("Answer: B")
    print()

    # ==============================================================================
    # END OF MCQS
    # ==============================================================================
    print("=" * 80)


if __name__ == "__main__":
    main()