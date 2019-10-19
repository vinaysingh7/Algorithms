'''  Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.



 Similar to maximum subarray of sum k but with sum as 0, so we need to convert all 0s to -1.
'''
class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        arr = [1 if item == 1 else -1 for item in nums]
        s = 0
        d = {}
        result  = 0
        max_len = 0
        d[0] = -1
        for i, item in enumerate(arr):
            s += item
            if s in d:
                max_len = max(max_len, i- d[s])
            else:
                 d[s] = i
        return max_len