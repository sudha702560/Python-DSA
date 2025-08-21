class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        unique_pos = 1

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                nums[unique_pos] = nums[i]
                unique_pos+=1
        
        return unique_pos