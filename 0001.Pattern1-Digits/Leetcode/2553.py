"""
---------------------------------------------------------------------------
|||||         Leetcode 2553: Separate the Digits in an Array
---------------------------------------------------------------------------
🧩 Problem:
Given an array of positive integers `nums`, return an array `answer` that consists of the digits of 
each integer in `nums` after separating them in the same order they appear.

To separate the digits of an integer is to get all the digits it has, in the same order.

📌 Examples:

Example 1:
Input: nums = [13, 25, 83, 77]
Output: [1, 3, 2, 5, 8, 3, 7, 7]
Explanation: 
- 13 → [1, 3]
- 25 → [2, 5]
- 83 → [8, 3]
- 77 → [7, 7]

Example 2:
Input: nums = [7, 1, 3, 9]
Output: [7, 1, 3, 9]

🛑 Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10⁵
"""

class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for num in nums:
            # Convert each number to a string to access individual digits
            num_str = str(num)
            for digit in num_str:
                result.append(int(digit))  # Convert character back to int and append

        return result
