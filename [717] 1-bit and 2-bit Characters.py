# Problem
'''
We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero.

Example - 
Input: [1, 0, 0]
Output: True
'''

# Solution: (Faster than 80.38% of python3 submissions)
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)
        while i < n-1:
            if bits[i] == 1:
                i += 2
            else:
                i += 1

        if i == n-1:
            return True
        return False
