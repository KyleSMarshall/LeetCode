# Problem:
'''
In a given grid, each cell can have one of three values:

    the value 0 representing an empty cell;
    the value 1 representing a fresh orange;
    the value 2 representing a rotten orange.

Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is 
impossible, return -1 instead.

Example -
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
'''


# Solution: (Faster than 90.44% of python3 solutions)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # Make a list of oranges that are rotten to begin with
        # These will be our starting points
        
        neighbors = [[] for i in range(len(grid) * len(grid[0]))]
        fresh = set()
        rotten = set()
        
        # Create a flat list of oranges
        flat_list = [item for sublist in grid for item in sublist]
        # Add the fresh and rotten indices to their appropriate set
        for i in range(len(flat_list)):
            if flat_list[i] == 1:
                fresh.add(i)
            elif flat_list[i] == 2:
                rotten.add(i)
        
        # Stop right away if we have no fresh oranges
        if len(fresh) == 0:
            return 0
        
        # Make neighboring associations in loop
        h = len(grid)
        l = len(grid[0])
        for i in range(h):
            for k in range(l):
                # Index location of orange in flattened grid
                orange_loc = i*l + k
                # Conditionals to ensure we don't query invalid indices
                if k != l-1:
                    if grid[i][k] != 0 and grid[i][k+1] != 0:
                        neighbors[orange_loc].append(orange_loc + 1)
                        neighbors[orange_loc + 1].append(orange_loc)
                        
                if i != h-1:
                    if grid[i][k] != 0 and grid[i+1][k] != 0:
                        neighbors[orange_loc].append(orange_loc + l)
                        neighbors[orange_loc + l].append(orange_loc)

        
        # Use depth-breadth-search algorithm
        def dbs(graph, start):
            
            visited, queue = set(), start
            time = 0
            
            while queue:
                new_queue = queue[:]
                time_inc = False # Default to not increase time
                
                while new_queue:
                    vertex = new_queue.pop(0)
                    queue.remove(vertex)
                    
                    if vertex not in visited:
                        visited.add(vertex)
                        for v in graph[vertex]:
                            if v not in visited and v not in queue:
                                queue.extend([v])
                                time_inc = True
                                
                if time_inc == True: 
                    time += 1

            return (visited, time)
        
        rotten_start = list(rotten)
        visited, time = dbs(neighbors, rotten_start)
        
        # Return -1 if there are remaining fresh oranges
        if len(visited) != len(fresh)+len(rotten):
            return -1
        
        return time
