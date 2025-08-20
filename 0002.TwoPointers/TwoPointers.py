"""
 ---------------------------------------------------------------
|                                                               |
|                      Two Pointers Approach                    |
|                                                               |
 ---------------------------------------------------------------

1. Reverse String  
   - LeetCode Link: [Reverse String](https://leetcode.com/problems/reverse-string/)  
   - Example: Input: "hello" → Output: "olleh"

2. Valid Palindrome  
   - LeetCode Link: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)  
   - Example: Input: "racecar" → Output: True  
   - Note: Also includes ignoring non-alphanumeric characters, e.g., "A man, a plan, a canal: Panama" → True

3. Move Zeroes  
   - LeetCode Link: [Move Zeroes](https://leetcode.com/problems/move-zeroes/)  
   - Example: Input: [0, 1, 0, 3] → Output: [1, 3, 0, 0]

4. Remove Duplicates from Sorted Array  
   - LeetCode Link: [Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)  
   - Example: Input: [1, 1, 2, 3] → Output: 3, Modified Array: [1, 2, 3]

5. Two Sum II - Input Array Is Sorted  
   - LeetCode Link: [Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)  
   - Example: Input: [1, 2, 3, 4], target = 5 → Output: [1, 4]

6. Merge Sorted Array  
   - LeetCode Link: [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)  
   - Example: Input: [1, 3], [2, 4] → Output: [1, 2, 3, 4]

7. Check if Array Is Sorted and Rotated (Related)  
   - LeetCode Link: [Check If Array Is Sorted and Rotated](https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/)  
   - Example: Input: [1, 2, 2, 3] → Output: True

8. Intersection of Two Arrays  
   - LeetCode Link: [Intersection of Two Arrays](https://leetcode.com/problems/intersection-of-two-arrays/)  
   - Example: Input: [1, 2, 4], [2, 4, 6] → Output: [2, 4]

9. Swap Nodes in Pairs (Linked List)  
   - LeetCode Link: [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)  
   - Example: Input: [1, 2, 3, 4] → Output: [2, 1, 4, 3]

10. Reverse Vowels of a String  
    - LeetCode Link: [Reverse Vowels of a String](https://leetcode.com/problems/reverse-vowels-of-a-string/)  
    - Example: Input: "hello" → Output: "holle"

11. Middle of the Linked List (Related)  
    - LeetCode Link: [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)  
    - Example: Input: [1, 2, 3, 4, 5] → Output: 3

12. Partition Array According to Given Pivot  
    - LeetCode Link: [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot/)  
    - Example: Input: [3, 1, 4, 2], val=3 → Output: [1, 2, 4, 3]

13. 3Sum Closest (Related)  
    - LeetCode Link: [3Sum Closest](https://leetcode.com/problems/3sum-closest/)  
    - Example: Input: [1, 2, 3, 4], target = 6 → Output: [2, 4]

14. Remove Element  
    - LeetCode Link: [Remove Element](https://leetcode.com/problems/remove-element/)  
    - Example: Input: [3, 2, 2, 3], val = 3 → Output: 2, Modified Array: [2, 2]

15. Valid Anagram  
    - LeetCode Link: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)  
    - Example: Input: "cat", "act" → Output: True

16. Find First and Last Position of Element in Sorted Array  
    - LeetCode Link: [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)  
    - Example: Input: [1, 2, 2, 2, 3], target = 2 → Output: [1, 3]

17. Rotate Array (when k = 1)  
    - LeetCode Link: [Rotate Array](https://leetcode.com/problems/rotate-array/)  
    - Example: Input: [1, 2, 3, 4] → Output: [4, 1, 2, 3]

18. Count Number of Pairs with Absolute Difference K  
    - LeetCode Link: [Count Number of Pairs with Absolute Difference K](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/)  
    - Example: Input: [1, 2, 3, 4], diff = 1 → Output: 3 ([1,2], [2,3], [3,4])

19. Reverse Words in a String  
    - LeetCode Link: [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)  
    - Example: Input: "hello world" → Output: "world hello"

20. Contains Duplicate  
    - LeetCode Link: [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)  
    - Example: Input: [1, 2, 2, 3] → Output: True

21. Sort Array by Parity  
    - LeetCode Link: [Sort Array by Parity](https://leetcode.com/problems/sort-array-by-parity/)  
    - Example: Input: [3, 2, 4, 1] → Output: [2, 4, 3, 1]

22. Contiguous Array  
    - LeetCode Link: [Contiguous Array](https://leetcode.com/problems/contiguous-array/)  
    - Example: Input: [0, 1, 0, 1] → Output: 4

23. Two Sum  
    - LeetCode Link: [Two Sum](https://leetcode.com/problems/two-sum/)  
    - Example: Input: [3, 2, 4], target = 6 → Output: [1, 2]

24. Container With Most Water  
    - LeetCode Link: [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)  
    - Example: Input: [1, 8, 6, 2, 5] → Output: 40

25. 3Sum  
    - LeetCode Link: [3Sum](https://leetcode.com/problems/3sum/)  
    - Example: Input: [-1, 0, 1, 2, -1, -4] → Output: [[-1, -1, 2], [-1, 0, 1]]

26. Sort Colors  
    - LeetCode Link: [Sort Colors](https://leetcode.com/problems/sort-colors/)  
    - Example: Input: [2, 0, 1] → Output: [0, 1, 2]

27. Longest Substring with At Most Two Distinct Characters  
    - LeetCode Link: [Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/)  
    - Example: Input: "eceba" → Output: 3 ("ece")

28. Remove Nth Node from End of Linked List  
    - LeetCode Link: [Remove Nth Node from End of Linked List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)  
    - Example: Input: [1, 2, 3, 4, 5], n=2 → Output: [1, 2, 3, 5]

29. Trapping Rain Water  
    - LeetCode Link: [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)  
    - Example: Input: [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] → Output: 6

30. Longest Palindromic Substring  
    - LeetCode Link: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)  
    - Example: Input: "babad" → Output: "bab" or "aba"

31. Partition Equal Subset Sum  
    - LeetCode Link: [Partition Equal Subset Sum](https://leetcode.com/problems/partition-equal-subset-sum/)  
    - Example: Input: [1, 5, 11, 5] → Output: True

32. Minimum Window Substring  
    - LeetCode Link: [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)  
    - Example: Input: s="ADOBECODEBANC", t="ABC" → Output: "BANC"

33. Remove All Instances of Substring  
    - LeetCode Link: [Remove All Occurrences of a Substring](https://leetcode.com/problems/remove-all-occurrences-of-a-substring/)  
    - Example: Input: "daabcba", "abc" → Output: "daba"

34. Intersection of Two Linked Lists  
    - LeetCode Link: [Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)  
    - Example: Input: A: [1, 2, 3, 4], B: [5, 6, 3, 4] → Output: node with value 3

35. Sort Array by Parity  
    - LeetCode Link: [Sort Array by Parity](https://leetcode.com/problems/sort-array-by-parity/)  
    - Example: Input: [3, 1, 2, 4] → Output: [2, 4, 3, 1]

36. Find the Duplicate Number  
    - LeetCode Link: [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)  
    - Example: Input: [1, 2, 2, 3] → Output: 2

37. Rotate String  
    - LeetCode Link: [Rotate String](https://leetcode.com/problems/rotate-string/)  
    - Example: Input: "water", "terwa" → Output: True

38. Swap Nodes in Pairs  
    - LeetCode Link: [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)  
    - Example: Input: [1, 2, 3, 4] → Output: [2, 1, 4, 3]

39. Contiguous Array  
    - LeetCode Link: [Contiguous Array](https://leetcode.com/problems/contiguous-array/)  
    - Example: Input: [0, 1, 0, 1] → Output: 4

40. Remove Duplicates from Sorted List  
    - LeetCode Link: [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)  
    - Example: Input: [1, 1, 2, 3, 3] → Output: [1, 2, 3]

41. Minimum Size Subarray Sum  
    - LeetCode Link: [Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)  
    - Example: Input: nums = [2, 3, 1, 2, 4], target = 6 → Output: 2 ([3, 4])

42. Is Subsequence  
    - LeetCode Link: [Is Subsequence](https://leetcode.com/problems/is-subsequence/)  
    - Example: Input: s = "abc", t = "ahbgdc" → Output: True

43. Reverse Only Letters  
    - LeetCode Link: [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)  
    - Example: Input: "a-bC-d" → Output: "d-cB-a"

"""