# Problem:
'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''


# Solution: (Note that I wanted to challenge myself by not ever converting the number to a string. 
#            The problem would be a 1-2 liner otherwise.)
class Solution:
    def isPalindrome(self, x):
        # This is done without ever converting to string
        def int_splitter(x):

            mod = 10
            num_list = []

            while mod/10 <= x:

                num = x % mod
                num_list.append(int(num*10/mod))
                x = x - num
                mod = mod * 10

            return num_list
        if x < 0:
            return False
        elif x == 0:
            return True

        x = int_splitter(x)
        length = len(x)
        half_way = int(length/2)

        for i in range(0, half_way):
            if x[i] != x[length-1-i]:
                return False

        return True
