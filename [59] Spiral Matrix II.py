# The problem:

'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n**2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''

# Solution: (Faster than 98.34% of python3 submissions)

class Solution:
    def generateMatrix(self, n):
        
        # Create a blank matrix to begin
        matrix = [[[' '] for i in range(n)] for k in range(n)]
        # Create border conditions so that the spiral knows which direction to take
        left = 0
        top = 0
        right = n
        bottom = n
        
        # Initialize row and column indexers to 0
        r = 0
        c = 0
        num = 1
        
        while num <= n**2:
            matrix[r][c] = num
            
            # Conditions to change borders once a row/column is filled
            if r == top and c == right:
                bottom -= 1
            elif r == bottom and c == left:
                top += 1
            elif r == bottom and c == right and (r,c) != (n-1, n-1):
                left += 1
            elif r == top and c == left:
                right -= 1
            
            # Conditions to increment indices
            if r == top and c != right:
                cm = 1
                rm = 0
            elif r == bottom and c != left:
                cm = -1
                rm = 0
            elif c == left:
                rm = -1
                cm = 0
            elif c == right:
                rm = 1
                cm = 0
            c += cm
            r += rm
            num += 1
            
        return matrix
