# Problem:
'''
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is 
impossible, return -1 instead.
'''


# Solution: (Still in progress)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Make a list of oranges that are rotten to begin with
        # These will be our starting points
        
        oranges = [[] for i in range(len(grid) * len(grid[0]))]
        orange_set = set()
        
        # Make neighboring associations in loop
        for i in range(len(grid)):
            for k in range(len(grid)):
                orange_place = i*len(grid) + k
                if k != len(grid) -1:
                    if grid[i][k] != 0 and grid[i][k+1] != 0:
                        orange_set.add(orange_place)
                        orange_set.add(orange_place + 1)
                        oranges[orange_place].append(orange_place + 1)
                        oranges[orange_place + 1].append(orange_place)
                if i != len(grid)-1:
                    if grid[i][k] != 0 and grid[i+1][k] != 0:
                        orange_set.add(orange_place + len(grid))
                        orange_set.add(orange_place)
                        oranges[orange_place].append(orange_place+len(grid))
                        oranges[orange_place + len(grid)].append(orange_place)
        print(oranges)
        print(orange_set)
        
        # Use depth-breadth-search algorithm
        def dbs(graph, start):
            visited, queue = set(), [start]
            time = 0
            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    queue.extend(graph[vertex])
                
            return (visited, time)
        
        visited, time = dbs(oranges, 0)
        if len(visited) == len(orange_set):
            return time
        else:
            return -1
        
                
            
