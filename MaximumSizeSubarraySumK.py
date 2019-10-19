"""Q325 Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
If there isn't one, return 0 instead.

"""
class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s_dict = {}
        agg = 0
        result = 0
        for i, item in enumerate(nums):
            agg += item
            if agg == k:
                result = max(result, i+1)
            else:
                x = agg - k  # if curr_acc_sum(agg) - unwanted_part(x) = k, then subrray has sum k from x+1-> i
                if x in s_dict:
                    result = max(result, i - s_dict[x])
            if agg not in s_dict:
                s_dict[agg] = i
        return result