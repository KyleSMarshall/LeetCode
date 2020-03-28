# Problem:
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent 
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of 
money you can rob tonight without alerting the police.

Example - 
Input: [2,3,2]
Output: 3
'''

# Solution: (Faster than 74.15% of python3 submissions)
class Solution:
    
    def __init__(self):
        self.memory = {}
    
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Special cases when we have no homes or the first house is also the last house
        if not nums:
            return 0
        elif n == 1:
            return nums[0]
        
        # Obtain max money starting at the very first house
        firstHouse = self.DP(nums, 0, n-1)
        # Clear the cache since the last house will be allowed when starting at house 2 or 3
        self.memory = {}
        # Obtain max money starting at house 2 or 3
        notFirstHouse = max(self.DP(nums, 1, n), self.DP(nums, 2, n))
        return max(firstHouse, notFirstHouse)
    
    def DP(self, nums, house, last):
        '''
        Recursively returns the maximum money value when starting at a particular house
        and caches it in the memory dictionary with key = house and value = maximum$$.
        '''
        
        # Return 0 if house index exceeds the maximum value
        if house >= last:
            return 0
        
        # If we've visited this house on a previous iteration, return the value; no need to recalculate.
        if house in self.memory:
            return self.memory[house]
        
        # Set the house value to the maximum amount of money that can be gained by executing recursively.
        self.memory[house] = nums[house] + max(self.DP(nums, house+2, last), self.DP(nums, house+3, last))  
        return self.memory[house]
