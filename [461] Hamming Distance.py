# Problem:
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
'''


# Solution: (Faster than 98.34% of python3 submissions)
class Solution:
    def hammingDistance(self, x, y):
        return [(a==b) for a,b in zip('{0:031b}'.format(x),
                                      '{0:031b}'.format(y))].count(False)
