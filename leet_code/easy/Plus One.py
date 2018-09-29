"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        ten_digit = 10
        num = 0
        result = []
        
        
        for i in range(0,len(digits)):
            if i == len(digits)-1:
                num += digits[i]
            else:
                num += (digits[i]) * 10 ** (len(digits)-i-1)
        num += 1
        result = [int(x) for x in str(num)]
        
        return result
        
