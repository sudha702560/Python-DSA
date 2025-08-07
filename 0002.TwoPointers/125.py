"""
LeetCode Problem 125: Valid Palindrome

Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Examples:
    Input:  s = "A man, a plan, a canal: Panama"
    Output: True   # After filtering and lowercasing → "amanaplanacanalpanama"
    
    Input:  s = "race a car"
    Output: False  # After filtering → "raceacar"

Constraints:
    - 1 <= len(s) <= 2 * 10^5
    - s consists only of printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s):
        """
        Returns True if the given string is a palindrome (ignoring non-alphanumeric characters and case), otherwise False.
        
        :type s: str
        :rtype: bool
        """
        i, j = 0, len(s) - 1
        
        while i < j:
          
            while i < j and not s[i].isalnum():
                i += 1
            
            while i < j and not s[j].isalnum():
                j -= 1
            
    
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
