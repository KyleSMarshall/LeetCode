# Problem
'''
Given an integer array of size n, find all elements that appear more than (n/3) times.

Note: The algorithm should run in linear time and in O(1) space.

Example - 
Input: [3,2,3]
Output: [3]
'''

# Solution: (Faster than 60.39% of python3 submissiosn)
class Solution:
    def majorityElement(self, nums):    
        n = len(nums)/3
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        result = [numbers for numbers, count in counts.items() if count > n]
        
        return result
