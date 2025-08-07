"""
LeetCode Problem 344. Reverse String

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Input:  s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input:  s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Constraints:
- 1 <= s.length <= 10^5
- s[i] is a printable ASCII character.
"""

class Solution(object):
    def reverseString(self, s):
        """
        Reverses the input list of characters in-place.
        
        :type s: List[str]
        :rtype: None
        """
        i = 0
        j = len(s) - 1
    
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1



