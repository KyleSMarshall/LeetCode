# Problem:
'''
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example - 
Input: [1,0,0,0,1,0,1]
Output: 2
'''

# Solution: (Faster than 97.93% of python3 submissions)

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        L = -1          # left index tracker
        R = 0           # right index tracker
        max_ = 0        # max distance to nearest person
        maxLind = -1    # left index of the seat which provides max distance
        
        for i in range(len(seats)):
            if seats[i] == 1:
                R = i
                if max_ < (R-L)//2 and maxLind != -1:
                    max_ = (R-L)//2
                    maxLind = L    
                # Check first edge case
                elif max_ < (R-L) and maxLind == -1:
                    max_ = (R)
                    maxLind = 0 
                L = R
            # Check second edge case
            elif i == len(seats)-1:
                R = i
                if max_ < R-L:
                    return R-L    
        return max_ 
        
