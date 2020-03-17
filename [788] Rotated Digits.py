# Problem:
'''
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number 
that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 
2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not
rotate to any other number and become invalid.

Now given a positive number N, how many numbers X from 1 to N are good?

Example - 
Input: 10
Output: 4
Explanation: 
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
'''

# Solution: (Faster than 56.87% of python3 submissions)
class Solution: 
    def rotatedDigits(self, N: int) -> int:
        good_dig = ['2','5','6','9']
        bad_dig = ['3', '7', '4']
        count = 0
        
        for num in range(1, N+1):
            num_ = list(str(num))
            num_.reverse()
            for bad in bad_dig:
                if bad in num_:
                    break
            else: 
                for dig in good_dig:
                    if dig in num_:
                        count += 1
                        break
        return count
