"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix = []
        suffix = []
        result = []
        
        for num in nums:
            if prefix:
                prefix.append(prefix[-1] * num)
            else:
                prefix.append(num)
        
        for num in reversed(nums):
            if suffix:
                suffix.append(suffix[-1] * num)
            else:
                suffix.append(num)
        
        suffix = list(reversed(suffix))
        
        for i in range(0,len(nums)):
            if i == 0:
                result.append(suffix[i+1])
            elif i == len(nums)-1:
                result.append(prefix[i-1])
            else:
                result.append(prefix[i-1] * suffix[i+1])
        return result
