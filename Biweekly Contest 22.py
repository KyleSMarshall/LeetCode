''' 
This contest was comprised of 4 questions increasing in difficulty. The time limit to complete all 4 questions
was 1.5 hours.

I was able to complete 3/4 of the questions in 1.10 hours.

Most of the solutions to these questions are not submitted during the timed contest and have unlimited 
time to ponder and research the question in order to optimize their solution. I went with the first 
accepted solution some of which may be considered "brute force". I will revisit these questions at a 
later date and post an "optimized" solution.
'''


# Problem 1:
'''
[1385] - Find the Distance Value Between Two Arrays
Difficulty: Easy

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any 
element arr2[j] where |arr1[i]-arr2[j]| <= d.
'''
# Solution 1:
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        distance = 0
        for num1 in arr1:
            for num2 in arr2:
                dist = abs(num2-num1)
                if dist <= d:
                    break
            else:
                distance += 1
        return distance
    
    
    
# Problem 2:
'''
[1386] - Cinema Seat Allocation
Difficulty: Medium

A cinema has n rows of seats, numbered from 1 to n and there are ten seats in each row, 
labelled from 1 to 10 as shown in the figure above.

Given the array reservedSeats containing the numbers of seats already reserved, for example, 
reservedSeats[i]=[3,8] means the seat located in row 3 and labelled with 8 is already reserved. 

Return the maximum number of four-person families you can allocate on the cinema seats. A four-person 
family occupies fours seats in one row, that are next to each other. Seats across an aisle 
(such as [3,3] and [3,4]) are not considered to be next to each other, however, It is permissible for 
the four-person family to be separated by an aisle, but in that case, exactly two people have to sit on
each side of the aisle.
'''
# Solution 2:
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        reservedSeats = sorted(reservedSeats, key = lambda x: [x[0], x[1]])
        print(reservedSeats)
        
        numFams = 0
        rowNum = 1
        inc = 0
        searched_rows = 0
        # Conditionals
        while inc < len(reservedSeats):
            
            grid = [0 for x in range(10)]
            start = inc
            
            for row, seat in reservedSeats[start:]:
                #print(row, seat)
                if row != rowNum:
                    rowNum = row
                    #print('Break')
                    break
                else:
                    inc += 1
                    grid[seat-1] = 1
            #print('Row ', row,' grid is: ')
            #print(grid)
            
            found = False
            for seat in range(2, 10):
                if grid[seat-1] != 0:
                    break
            else:
                found = True
                numFams += 2
                
            if found != True:
                for seat in range(2, 6):
                    if grid[seat-1] != 0:
                        break
                else:
                    found = True
                    numFams += 1
                    
            if found != True:    
                for seat in range(6, 10):
                    if grid[seat-1] != 0:
                        break
                else:
                    found = True
                    numFams += 1
                    
            if found != True:
                for seat in range(4, 8):
                    if grid[seat-1] != 0:
                        break
                else:
                    found = True
                    numFams += 1
            searched_rows += 1
            
        numFams += (n-searched_rows)*2                   
        return numFams



# Problem 3:
'''
[1387] - Sort Integers by The Power Value
Difficulty: Medium

The power of an integer x is defined as the number of steps needed to transform x into 1 using the following steps:

    if x is even then x = x / 2
    if x is odd then x = 3 * x + 1

For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1 
(3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).

Given three integers lo, hi and k. The task is to sort all integers in the interval [lo, hi] by the power value
in ascending order, if two or more integers have the same power value sort them by ascending order.

Return the k-th integer in the range [lo, hi] sorted by the power value.

Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1 using these steps and 
that the power of x is will fit in 32 bit signed integer.
'''
# Solution 3:
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        power_list = []
        
        def power(num, i=0):
            if num == 1:
                return i
            if num % 2 == 0:
                i += 1
                num = num/2
                return power(num, i)
            else:
                i += 1
                num = 3 * num + 1
                return power(num, i)
        
        for num in range(lo, hi+1):
            power_list.append(power(num))
        
        num_range = range(lo, hi+1)
        nums = [x for x, _ in sorted(zip(num_range, power_list), key = lambda x: [x[1], x[0]])]
        
        return nums[k-1]
        
        
        
# Problem 4:
'''
[1388] - Pizza With 3n Slices
Difficulty: Hard

There is a pizza with 3n slices of varying size, you and your friends will take slices of pizza as follows:

    You will pick any pizza slice.
    Your friend Alice will pick next slice in anti clockwise direction of your pick. 
    Your friend Bob will pick next slice in clockwise direction of your pick.
    Repeat until there are no more slices of pizzas.

Sizes of Pizza slices is represented by circular array slices in clockwise direction.

Return the maximum possible sum of slice sizes which you can have.
'''
# Solution 4:
None
