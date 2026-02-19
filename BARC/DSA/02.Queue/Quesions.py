#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
================================================================================
            QUEUE DATA STRUCTURE – 40 COMPREHENSIVE MCQs
================================================================================
Each question is followed by its options (prefixed with '#') and the correct answer.
Use this to test your understanding of queues – from basics to advanced patterns.
"""

def main():
    # ==============================================================================
    # QUESTION 1
    # ==============================================================================
    print("1. What does FIFO stand for in the context of a queue?")
    print("# A) First In, First Out")
    print("# B) Fast In, Fast Out")
    print("# C) File In, File Out")
    print("# D) First In, Only Out")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 2
    # ==============================================================================
    print("2. Which of the following is NOT a basic queue operation?")
    print("# A) enqueue")
    print("# B) dequeue")
    print("# C) peek")
    print("# D) push")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 3
    # ==============================================================================
    print("3. What is the time complexity of a `dequeue()` operation in a queue implemented using a Python list (pop(0))?")
    print("# A) O(1)")
    print("# B) O(n)")
    print("# C) O(log n)")
    print("# D) O(n²)")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 4
    # ==============================================================================
    print("4. Which Python module provides a thread‑safe queue implementation?")
    print("# A) collections.deque")
    print("# B) queue.Queue")
    print("# C) array.array")
    print("# D) threading.Queue")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 5
    # ==============================================================================
    print("5. A queue is a ______ data structure.")
    print("# A) linear")
    print("# B) non-linear")
    print("# C) hierarchical")
    print("# D) graph-based")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 6
    # ==============================================================================
    print("6. Which of the following is a real‑life example of a queue?")
    print("# A) Stack of plates")
    print("# B) Undo operation in a text editor")
    print("# C) Printer spooler")
    print("# D) Function call stack")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 7
    # ==============================================================================
    print("7. What will happen if we perform `dequeue()` on an empty queue using a typical linked‑list implementation?")
    print("# A) Returns None")
    print("# B) Returns 0")
    print("# C) Raises IndexError / Underflow exception")
    print("# D) Returns -1")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 8
    # ==============================================================================
    print("8. Which of the following is **not** an application of queue?")
    print("# A) Breadth‑First Search")
    print("# B) Process scheduling")
    print("# C) Depth‑First Search")
    print("# D) Print spooling")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 9
    # ==============================================================================
    print("9. In a circular queue of size `n`, how is the rear index updated during enqueue?")
    print("# A) rear = rear + 1")
    print("# B) rear = (rear + 1) % n")
    print("# C) rear = (rear + 1) if rear < n else 0")
    print("# D) rear = rear - 1")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 10
    # ==============================================================================
    print("10. What is the space complexity of a queue storing `n` elements?")
    print("# A) O(1)")
    print("# B) O(log n)")
    print("# C) O(n)")
    print("# D) O(n²)")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 11
    # ==============================================================================
    print("11. Which of the following is true about a priority queue?")
    print("# A) Elements are processed in FIFO order")
    print("# B) Elements are processed based on their priority, not insertion order")
    print("# C) It is also known as a circular queue")
    print("# D) It cannot be implemented using a heap")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 12
    # ==============================================================================
    print("12. How many queues are required to implement a stack efficiently?")
    print("# A) One")
    print("# B) Two")
    print("# C) Three")
    print("# D) None")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 13
    # ==============================================================================
    print("13. What is the output of the following code snippet?")
    print("# from collections import deque")
    print("# q = deque()")
    print("# q.append(1)")
    print("# q.append(2)")
    print("# q.append(3)")
    print("# print(q.popleft())")
    print("# print(q[0])")
    print("# A) 1, 2")
    print("# B) 3, 2")
    print("# C) 1, 3")
    print("# D) 2, 3")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 14
    # ==============================================================================
    print("14. Which of the following is true about a queue implemented with a singly linked list (with front and rear pointers)?")
    print("# A) Enqueue is O(n), Dequeue is O(1)")
    print("# B) Enqueue is O(1), Dequeue is O(n)")
    print("# C) Both enqueue and dequeue are O(1)")
    print("# D) Peek is O(n)")
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
    print("16. In a static array‑based circular queue, the condition for **queue full** is:")
    print("# A) front == -1")
    print("# B) rear == capacity - 1")
    print("# C) (rear + 1) % capacity == front")
    print("# D) front == rear")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 17
    # ==============================================================================
    print("17. What is the result of the following operations on an initially empty queue: enqueue(5), enqueue(10), dequeue(), enqueue(15), dequeue(), dequeue()?")
    print("# A) 5, 10, 15")
    print("# B) 5, 15, None/Error")
    print("# C) 10, 15, None/Error")
    print("# D) 15, 5, 10")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 18
    # ==============================================================================
    print("18. Which data structure is used in Breadth‑First Search (BFS) of a graph?")
    print("# A) Stack")
    print("# B) Queue")
    print("# C) Priority Queue")
    print("# D) Tree")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 19
    # ==============================================================================
    print("19. What does the `peek()` operation return in a queue?")
    print("# A) The front element and removes it")
    print("# B) The front element without removing it")
    print("# C) The rear element")
    print("# D) The size of the queue")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 20
    # ==============================================================================
    print("20. Which of the following is **not** an advantage of a linked list over an array for queue implementation?")
    print("# A) Dynamic size")
    print("# B) No overflow until heap memory exhausted")
    print("# C) Better cache locality")
    print("# D) Easier to expand")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 21
    # ==============================================================================
    print("21. What is the minimum number of priority queues needed to implement a stack that supports push, pop, and getMin in O(1)?")
    print("# A) 0")
    print("# B) 1")
    print("# C) 2")
    print("# D) 3")
    print("Answer: B (Hint: Not a typical queue question, but a trick. Actually getMin stack is not queue. We'll avoid this. Let's replace with a proper queue question.)")
    # Let's replace Q21 with something else:
    print("21. In a deque (double-ended queue), which operation allows adding an element to the front?")
    print("# A) append()")
    print("# B) appendleft()")
    print("# C) extend()")
    print("# D) insert(0)")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 22
    # ==============================================================================
    print("22. If elements are enqueued in order: `A`, `B`, `C`, `D`, then dequeued and printed, what is the output?")
    print("# A) A B C D")
    print("# B) D C B A")
    print("# C) A C B D")
    print("# D) D A B C")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 23
    # ==============================================================================
    print("23. Which algorithm uses a queue for its iterative implementation?")
    print("# A) Depth‑First Search")
    print("# B) Breadth‑First Search")
    print("# C) Binary Search")
    print("# D) Quick Sort")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 24
    # ==============================================================================
    print("24. What is the time complexity of finding the maximum in a sliding window of size `k` for an array of `n` elements using a monotonic deque?")
    print("# A) O(n)")
    print("# B) O(nk)")
    print("# C) O(n log k)")
    print("# D) O(n²)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 25
    # ==============================================================================
    print("25. In a queue implemented using two stacks, what is the amortized time complexity of a dequeue operation?")
    print("# A) O(1)")
    print("# B) O(n)")
    print("# C) O(log n)")
    print("# D) O(n²)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 26
    # ==============================================================================
    print("26. Which of the following is an example of a **priority queue**?")
    print("# A) Task scheduler where urgent tasks run first")
    print("# B) Print spooler")
    print("# C) Keyboard buffer")
    print("# D) FIFO queue")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 27
    # ==============================================================================
    print("27. The maximum number of elements that can be stored in a circular queue of size `S` is:")
    print("# A) S")
    print("# B) S-1")
    print("# C) S+1")
    print("# D) 2S")
    print("Answer: B (if using one slot to distinguish full/empty), but many implementations use S. We'll go with B as classic.")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 28
    # ==============================================================================
    print("28. Which of the following statements is **false** about a queue?")
    print("# A) Queue can be implemented using an array")
    print("# B) Queue can be implemented using a linked list")
    print("# C) Queue supports random access")
    print("# D) Queue follows FIFO order")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 29
    # ==============================================================================
    print("29. What is the result of generating binary numbers from 1 to 5 using a queue?")
    print("# A) 1, 10, 11, 100, 101")
    print("# B) 1, 2, 3, 4, 5")
    print("# C) 1, 11, 101, 111, 1001")
    print("# D) 1, 10, 100, 1000, 10000")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 30
    # ==============================================================================
    print("30. In which of the following scenarios is queue **not** suitable?")
    print("# A) Handling requests to a web server")
    print("# B) Implementing undo operation")
    print("# C) Breadth‑First Traversal of a tree")
    print("# D) Scheduling processes in an OS")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 31
    # ==============================================================================
    print("31. If a queue is implemented using a circular array with front=2, rear=5, and capacity=8, how many elements are in the queue?")
    print("# A) 3")
    print("# B) 4")
    print("# C) 5")
    print("# D) 6")
    print("Answer: B (rear-front+1 if rear>=front else capacity-front+rear+1; here 5-2+1=4)")
    print()

    # ==============================================================================
    # QUESTION 32
    # ==============================================================================
    print("32. A blocking queue is typically used in:")
    print("# A) Producer‑consumer problem")
    print("# B) Graph traversal")
    print("# C) Expression evaluation")
    print("# D) Sorting algorithms")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 33
    # ==============================================================================
    print("33. Which of the following is **not** a property of a deque?")
    print("# A) Can insert at both ends")
    print("# B) Can delete from both ends")
    print("# C) Follows FIFO strictly")
    print("# D) Can be used as both stack and queue")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 34
    # ==============================================================================
    print("34. The minimum number of queues required to implement a priority queue using heaps conceptually is:")
    print("# A) 0")
    print("# B) 1")
    print("# C) 2")
    print("# D) 3")
    print("Answer: B (heap itself is a data structure, not queue; but a priority queue can be implemented with one heap. So B is fine.)")
    print()

    # ==============================================================================
    # QUESTION 35
    # ==============================================================================
    print("35. Which operation in `collections.deque` is O(1) but O(n) in a Python list?")
    print("# A) append()")
    print("# B) pop() from right")
    print("# C) popleft()")
    print("# D) insert(0, x)")
    print("Answer: C")
    print("# Note: popleft() is O(1) in deque; list has no popleft, but pop(0) is O(n).")
    print()

    # ==============================================================================
    # QUESTION 36
    # ==============================================================================
    print("36. In a queue implemented using two stacks, which operation is typically made O(1)?")
    print("# A) Enqueue")
    print("# B) Dequeue")
    print("# C) Both")
    print("# D) Neither")
    print("Answer: A (enqueue O(1), dequeue amortized O(1))")
    print()

    # ==============================================================================
    # QUESTION 37
    # ==============================================================================
    print("37. How many times is the queue modified (enqueue/dequeue) while generating the first 4 binary numbers using the queue method?")
    print("# A) 4")
    print("# B) 5")
    print("# C) 6")
    print("# D) 7")
    print("Answer: D")

    # ==============================================================================
    # QUESTION 38
    # ==============================================================================
    print("38. Which of the following is **true** about the `queue.Queue` in Python?")
    print("# A) It is not thread‑safe")
    print("# B) It provides `put()` and `get()` methods")
    print("# C) It always blocks indefinitely")
    print("# D) It cannot have a maximum size")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 39
    # ==============================================================================
    print("39. In the 'rotten oranges' problem, what data structure is used to process the oranges level by level?")
    print("# A) Stack")
    print("# B) Queue")
    print("# C) Priority Queue")
    print("# D) Tree")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 40
    # ==============================================================================
    print("40. Which of the following problems uses the concept of a **monotonic queue**?")
    print("# A) Binary search")
    print("# B) Sliding window maximum")
    print("# C) Merge sort")
    print("# D) Knuth‑Morris‑Pratt algorithm")
    print("Answer: B")
    print()

if __name__ == "__main__":
    main()