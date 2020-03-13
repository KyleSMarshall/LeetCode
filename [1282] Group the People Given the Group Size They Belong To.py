# Problem:
'''
There are n people whose IDs go from 0 to n - 1 and each person belongs exactly to one group. Given the 
array groupSizes of length n telling the group size each person belongs to, return the groups there are 
and the people's IDs each group includes.

You can return any solution in any order and the same applies for IDs. Also, it is guaranteed that there 
exists at least one solution. 

Example -
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]
Explanation: 
Other possible solutions are [[2,1,6],[5],[0,4,3]] and [[5],[0,6,2],[4,3,1]].
'''


# Solution: (Faster than 32.11% of python3 submissions)
class Solution:
    def groupThePeople(self, groupSizes):

        # Create a dict to keep track of the group sizes and the number of counts
        # for each size in order to determine how many groups of that size we need
        group_counts = {}
        group_ids = {}

        for person_id, group_size in enumerate(groupSizes):
            if group_size in group_counts:
                group_counts[group_size] += 1
                group_ids[group_size].append(person_id)

            else:
                group_counts[group_size] = 1
                group_ids[group_size] = [person_id]

        output = []

        # Now we need to split the str of person_ids
        for i, j in group_counts.items():
            num_groups = int(j/i)
            temp_group = set(group_ids[i])

            # Now add these people to their groups
            for k in range(num_groups):
                new_group = []
                for m in range(i):
                    new_group.append(temp_group.pop())
                output.append(new_group)

        return output
