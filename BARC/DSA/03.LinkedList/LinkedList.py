"""
================================================================================
          LINKED LIST DATA STRUCTURE – 40 COMPREHENSIVE MCQs
================================================================================

"""

def main():
    # ==============================================================================
    # QUESTION 1
    # ==============================================================================
    print("1. What is a linked list?")
    print("# A) A linear data structure where elements are stored in contiguous memory locations")
    print("# B) A linear data structure where elements are stored in nodes with pointers to the next node")
    print("# C) A non-linear data structure where each node points to two children")
    print("# D) A data structure that follows FIFO order")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 2
    # ==============================================================================
    print("2. Which of the following is NOT a type of linked list?")
    print("# A) Singly linked list")
    print("# B) Doubly linked list")
    print("# C) Circular linked list")
    print("# D) Binary linked list")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 3
    # ==============================================================================
    print("3. In a singly linked list, each node contains:")
    print("# A) Data and a pointer to the previous node")
    print("# B) Data and a pointer to the next node")
    print("# C) Only data")
    print("# D) Data and pointers to both next and previous nodes")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 4
    # ==============================================================================
    print("4. What is the time complexity of inserting a node at the beginning of a singly linked list?")
    print("# A) O(1)")
    print("# B) O(n)")
    print("# C) O(log n)")
    print("# D) O(n²)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 5
    # ==============================================================================
    print("5. What is the time complexity of deleting the last node in a singly linked list (without a tail pointer)?")
    print("# A) O(1)")
    print("# B) O(n)")
    print("# C) O(log n)")
    print("# D) O(n²)")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 6
    # ==============================================================================
    print("6. Which data structure is used to implement an LRU cache efficiently?")
    print("# A) Singly linked list")
    print("# B) Array")
    print("# C) Doubly linked list + hashmap")
    print("# D) Circular queue")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 7
    # ==============================================================================
    print("7. How do you detect a cycle in a linked list?")
    print("# A) Using two pointers moving at different speeds")
    print("# B) Using a single pointer and checking for null")
    print("# C) Using a stack")
    print("# D) Using a queue")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 8
    # ==============================================================================
    print("8. What is the space complexity of a linked list with n nodes?")
    print("# A) O(1)")
    print("# B) O(log n)")
    print("# C) O(n)")
    print("# D) O(n²)")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 9
    # ==============================================================================
    print("9. Which of the following is an advantage of linked lists over arrays?")
    print("# A) Random access")
    print("# B) Better cache locality")
    print("# C) Dynamic size")
    print("# D) Less memory overhead")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 10
    # ==============================================================================
    print("10. What is the output of reversing a singly linked list: 1->2->3->4?")
    print("# A) 1->2->3->4")
    print("# B) 4->3->2->1")
    print("# C) 2->1->4->3")
    print("# D) 3->2->1->4")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 11
    # ==============================================================================
    print("11. In a doubly linked list, how many pointers are updated when inserting a node at the beginning?")
    print("# A) 1")
    print("# B) 2")
    print("# C) 3")
    print("# D) 4")
    print("Answer: B (the new node's next and previous; head's previous; and head itself)")
    print()

    # ==============================================================================
    # QUESTION 12
    # ==============================================================================
    print("12. Which of the following is NOT an application of linked lists?")
    print("# A) Implementing stacks and queues")
    print("# B) Graph adjacency lists")
    print("# C) Binary search")
    print("# D) Music player playlists")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 13
    # ==============================================================================
    print("13. How do you find the middle of a linked list in one pass?")
    print("# A) Count the nodes then traverse again")
    print("# B) Use two pointers, one moving twice as fast")
    print("# C) Use a stack to store all nodes")
    print("# D) Use recursion")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 14
    # ==============================================================================
    print("14. What is the time complexity of searching for an element in a sorted linked list?")
    print("# A) O(1)")
    print("# B) O(log n)")
    print("# C) O(n)")
    print("# D) O(n log n)")
    print("Answer: C")
    print()

    # ==============================================================================
    # QUESTION 15
    # ==============================================================================
    print("15. Which algorithm is used to detect the start of a cycle in a linked list?")
    print("# A) Floyd's cycle detection algorithm")
    print("# B) Kahn's algorithm")
    print("# C) Kruskal's algorithm")
    print("# D) Prim's algorithm")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 16
    # ==============================================================================
    print("16. In a circular linked list, the last node points to:")
    print("# A) NULL")
    print("# B) The head node")
    print("# C) The previous node")
    print("# D) Itself")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 17
    # ==============================================================================
    print("17. What is the advantage of a doubly linked list over a singly linked list?")
    print("# A) Less memory usage")
    print("# B) Easier to reverse traverse")
    print("# C) Faster search")
    print("# D) Simpler implementation")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 18
    # ==============================================================================
    print("18. Which of the following is true about skip lists?")
    print("# A) They use extra pointers for faster search")
    print("# B) They are a type of balanced tree")
    print("# C) They cannot have duplicates")
    print("# D) They are always sorted in descending order")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 19
    # ==============================================================================
    print("19. How do you reverse a singly linked list recursively?")
    print("# A) Reverse the rest and then adjust pointers")
    print("# B) Use a stack to reverse")
    print("# C) Swap data of nodes")
    print("# D) It cannot be done recursively")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 20
    # ==============================================================================
    print("20. What is the time complexity of merging two sorted linked lists?")
    print("# A) O(m + n)")
    print("# B) O(m * n)")
    print("# C) O(log(m + n))")
    print("# D) O(1)")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 21
    # ==============================================================================
    print("21. Which of the following problems can be solved using Floyd's cycle detection algorithm?")
    print("# A) Finding the middle of a linked list")
    print("# B) Detecting a cycle in a linked list")
    print("# C) Reversing a linked list")
    print("# D) Merging two sorted linked lists")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 22
    # ==============================================================================
    print("22. In a linked list, what does a dummy node help with?")
    print("# A) Reducing memory usage")
    print("# B) Simplifying edge cases when head may change")
    print("# C) Improving search time")
    print("# D) Implementing recursion")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 23
    # ==============================================================================
    print("23. How many pointers are needed to reverse a singly linked list iteratively?")
    print("# A) 1")
    print("# B) 2")
    print("# C) 3")
    print("# D) 4")
    print("Answer: C (previous, current, next)")
    print()

    # ==============================================================================
    # QUESTION 24
    # ==============================================================================
    print("24. Which of the following is NOT a characteristic of a linked list?")
    print("# A) Dynamic size")
    print("# B) Random access")
    print("# C) Sequential access")
    print("# D) Efficient insertion at ends")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 25
    # ==============================================================================
    print("25. What is the result of adding two numbers represented by linked lists: 2->4->3 and 5->6->4 (both in reverse order, i.e., 342 + 465)?")
    print("# A) 7->0->8")
    print("# B) 8->0->7")
    print("# C) 7->1->8")
    print("# D) 8->1->7")
    print("Answer: A (342 + 465 = 807, reversed is 7->0->8)")
    print()

    # ==============================================================================
    # QUESTION 26
    # ==============================================================================
    print("26. In a doubly linked list, deleting a node with a given pointer requires updating how many pointers?")
    print("# A) 1")
    print("# B) 2")
    print("# C) 3")
    print("# D) 4")
    print("Answer: B (previous node's next, next node's prev, and handling head/tail)")
    print()

    # ==============================================================================
    # QUESTION 27
    # ==============================================================================
    print("27. Which of the following is used to implement a memory-efficient doubly linked list?")
    print("# A) XOR linked list")
    print("# B) Circular linked list")
    print("# C) Skip list")
    print("# D) Unrolled linked list")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 28
    # ==============================================================================
    print("28. What is the time complexity to access the k-th element in a linked list?")
    print("# A) O(1)")
    print("# B) O(k)")
    print("# C) O(log k)")
    print("# D) O(n) where n is total nodes")
    print("Answer: D (since you must traverse from head)")
    print()

    # ==============================================================================
    # QUESTION 29
    # ==============================================================================
    print("29. Which of the following sorting algorithms is most suitable for linked lists?")
    print("# A) Quick sort")
    print("# B) Merge sort")
    print("# C) Heap sort")
    print("# D) Bubble sort")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 30
    # ==============================================================================
    print("30. How do you check if a linked list is a palindrome?")
    print("# A) Reverse the list and compare")
    print("# B) Use a stack to store first half and compare")
    print("# C) Use two pointers (slow/fast) and a stack")
    print("# D) All of the above")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 31
    # ==============================================================================
    print("31. What is the space complexity of reversing a linked list recursively?")
    print("# A) O(1)")
    print("# B) O(log n)")
    print("# C) O(n)")
    print("# D) O(n²)")
    print("Answer: C (due to recursion stack)")
    print()

    # ==============================================================================
    # QUESTION 32
    # ==============================================================================
    print("32. Which of the following is true about XOR linked list?")
    print("# A) It uses less memory by storing XOR of previous and next pointers")
    print("# B) It allows O(1) access to any node")
    print("# C) It can only be traversed in one direction")
    print("# D) It is the same as a doubly linked list")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 33
    # ==============================================================================
    print("33. In a linked list, how do you remove duplicates from an unsorted list?")
    print("# A) Use a hash set to track seen values")
    print("# B) Sort the list first")
    print("# C) Use two nested loops")
    print("# D) All of the above")
    print("Answer: D (multiple approaches exist)")
    print()

    # ==============================================================================
    # QUESTION 34
    # ==============================================================================
    print("34. What is the output of finding the intersection of two lists: 1->2->3->4 and 5->6->3->4? (Assume intersection by reference)")
    print("# A) 3")
    print("# B) 4")
    print("# C) 3->4")
    print("# D) No intersection")
    print("Answer: C (if nodes 3 and 4 are shared, the intersection starts at 3)")
    print()

    # ==============================================================================
    # QUESTION 35
    # ==============================================================================
    print("35. Which data structure is used to implement adjacency lists in graphs?")
    print("# A) Array of linked lists")
    print("# B) Array of arrays")
    print("# C) Hash table")
    print("# D) Queue")
    print("Answer: A")
    print()

    # ==============================================================================
    # QUESTION 36
    # ==============================================================================
    print("36. What happens when you try to access the next pointer of a None node?")
    print("# A) Returns None")
    print("# B) Raises AttributeError")
    print("# C) Returns 0")
    print("# D) Causes segmentation fault / program crash")
    print("Answer: B (in Python, AttributeError)")
    print()

    # ==============================================================================
    # QUESTION 37
    # ==============================================================================
    print("37. How do you rotate a linked list to the right by k places?")
    print("# A) Make the list circular, then break at appropriate point")
    print("# B) Reverse the list, then reverse parts")
    print("# C) Move the last k nodes to the front")
    print("# D) All of the above are possible")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 38
    # ==============================================================================
    print("38. Which of the following is NOT a way to reverse a linked list?")
    print("# A) Iterative method using three pointers")
    print("# B) Recursive method")
    print("# C) Using a stack")
    print("# D) Using a queue")
    print("Answer: D")
    print()

    # ==============================================================================
    # QUESTION 39
    # ==============================================================================
    print("39. In a linked list with a cycle, what happens if you traverse using a single pointer?")
    print("# A) It will eventually reach NULL")
    print("# B) It will loop infinitely")
    print("# C) It will raise an error")
    print("# D) It will stop after n steps")
    print("Answer: B")
    print()

    # ==============================================================================
    # QUESTION 40
    # ==============================================================================
    print("40. Which of the following is a disadvantage of linked lists?")
    print("# A) Dynamic size")
    print("# B) No memory wastage")
    print("# C) Extra memory for pointers")
    print("# D) Efficient insertion/deletion")
    print("Answer: C")
    print()

if __name__ == "__main__":
    main()
