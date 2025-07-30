"""
--------------------------------------------------------------------
        Leetcode 1796: Second Largest Digit in a String
--------------------------------------------------------------------

🧩 Problem:
Given an alphanumeric string `s`, return the **second largest numerical digit** that appears in `s`,
or -1 if it does not exist.

An alphanumeric string is a string consisting of **lowercase English letters and digits**.

📌 Examples:
Example 1:
Input: s = "dfa12321afd"
Output: 2
Explanation: The digits that appear in s are [1, 2, 3]. The second largest digit is 2.

Example 2:
Input: s = "abc1111"
Output: -1
Explanation: The only digit is 1. No second largest exists.

🛑 Constraints:
- 1 <= s.length <= 500
- s consists of only lowercase English letters and digits
"""

class Solution(object):
    def secondHighest(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = set()
        # digits = {int(char) for char in s if char.isdigit()}
        # Extract digits from the string
        for char in s:
            if char.isdigit():
                digits.add(int(char))
        
        # Return -1 if there are fewer than two distinct digits
        if len(digits) < 2:
            return -1 
        
        return self.find_second_highest(digits)

    def find_second_highest(self, digits):
        """
        Helper method to find the second largest digit from a set.
        :type digits: Set[int]
        :rtype: int
        """
        max1 = float("-inf")  # Largest digit
        max2 = float("-inf")  # Second largest digit

        for num in digits:
            if num > max1:
                max2 = max1
                max1 = num 
            elif num < max1 and num > max2:
                max2 = num 
            
        return max2 if max2 != float("-inf") else -1

