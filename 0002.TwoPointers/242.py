"""
242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"

Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        char_count ={}

        for char in s:
            char_count[char] = char_count.get(char,0) + 1
        
        for char in t:
            if char not in char_count:
                return False 
            char_count[char]-=1
            if char_count[char]==0:
                del char_count[char]
            
        return len(char_count)==0
    

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for char_s, char_t in zip(s, t):
            count[ord(char_s) - ord('a')] += 1
            count[ord(char_t) - ord('a')] -= 1
        return all(c == 0 for c in count)

"""

"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
"""


"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        # Count frequencies for s
        for char in s:
            count[ord(char) - ord('a')] += 1
        # Decrement frequencies for t
        for char in t:
            count[ord(char) - ord('a')] -= 1
            if count[ord(char) - ord('a')] < 0:
                return False
        # Check for non-zero counts
        for c in count:
            if c != 0:
                return False
        return True
"""