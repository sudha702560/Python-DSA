class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # zbax
        num_str =""

        for char in s:
            position = ord(char) - ord('a') +1

            num_str +=str(position)


            # run a loop k times and gind the digit sum 
    
