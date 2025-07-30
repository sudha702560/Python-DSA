"""
--------------------------------------------------------------------------
||||||      Leetcode 1295: Find Numbers with Even Number of Digits
--------------------------------------------------------------------------

🧩 Problem:
Given an array `nums` of integers, return how many of them contain an even number of digits.

📌 Example 1:
Input: nums = [12, 345, 2, 6, 7896]
Output: 2
Explanation: 
- 12 has 2 digits (even)
- 345 has 3 digits (odd)
- 2 has 1 digit (odd)
- 6 has 1 digit (odd)
- 7896 has 4 digits (even)

So, 12 and 7896 → total = 2

📌 Example 2:
Input: nums = [555, 901, 482, 1771]
Output: 1 
Explanation: Only 1771 has even number of digits

🛑 Constraints:
- 1 <= nums.length <= 500
- 1 <= nums[i] <= 10⁵
"""

import math

# ✅ Method 1: Using math (log10)
class SolutionMath(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            digits = int(math.log10(num)) + 1  # log10 gives digit count
            if digits % 2 == 0:
                count += 1
        return count


# ✅ Method 2: Using string conversion
class SolutionString(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

