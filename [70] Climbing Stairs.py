# Problem
'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
'''


# Solution: (Faster than 56.65% of python3 submissions)
class Solution:
    def climbStairs(self, n):
        
        import math

        def num_of_steps(n):
            return int(n/2)+1

        def permutations(N, num_twos):
            return int(math.factorial(N)/(math.factorial(N-num_twos) * math.factorial(num_twos)))

        distinct_ways = 0

        N = num_of_steps(n)

        for i in range(0, N):
            distinct_ways += permutations(n - i, i)

        return distinct_ways
