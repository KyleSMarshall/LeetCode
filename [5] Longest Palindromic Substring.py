# Problem:
'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example - 
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
'''

# Solution: (Faster than 56.03% of python3 submissions)
class Solution:
    
    def __init__(self):
        self.return_str = ''
        self.max_ = 1
    
    
    def helper(self, s: str, L: int, R: int) -> str:
        '''
        Recursive character comparison algorithm which checks if L and R index characters are the same.
        If so, decrease the L index and increase the R index and repeat the check. Do this until
        characters do not match.
        '''
        
        # Terminate if index out of range
        if L < 0 or R >= len(s):
            return self.return_str
        
        # Compare characters
        if s[L] == s[R]:
            self.return_str = s[L:R+1]
            R += 1
            L -= 1
            # Recursion
            self.helper(s, L, R)

        return self.return_str
        
    
    def longestPalindrome(self, s: str) -> str:
        '''
        Makes use of helper recursive function to return the longest palindromic substring in s.
        Loops through starting indices beginning at 0 and passes that value to the helper function
        to initiate its first run at that particular starting point.
        '''
        
        if s == '':
            return ''
        largest = s[0]
        
        i = 0
        max_range = len(s)
        initial_range = max_range
        
        while i < max_range:
            even = self.helper(s, L=i, R=i+1)
            odd = self.helper(s, L=i, R=i+2) 
            length = max(len(even), len(odd))
            
            if length > self.max_:
                self.max_ = length
                ind = length // 2
                om = 1 + length % 2
                largest = s[i-ind+1:i+ind+om]
            
            i += 1
            # If the current max_ is larger than the possible remaining
            # substrings, we should quit the loop to save time.
            max_range = initial_range - self.max_//2
            
        return largest
