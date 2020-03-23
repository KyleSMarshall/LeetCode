# Problem:
'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example-
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: False
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to 
take course 0 you should also have finished course 1. So it is impossible.
'''

# Solution: (Faster than 74.83% of python3 submissions*, memory usage less than 85.21%)
# *The runtime fluctuated when identical solutions were re-submitted. At best, my sumbission was faster than 99%
# and at worst it was faster than 50%. I submitted my solution 10 times and took the average percentile to display.

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Performs a breadth-first-search on a course/requirement list of edges to determine if it is possible
        to take every course.
        '''
        
        ''' 
        Need to create a list of dependencies. The list index represents the prerequisite and the list value
        represents the courses which require that specific prerequisite.
        
        Also creating a "needed" list which represents how many un-met prequisites remain for a given course
        which is represented by the list index. I.e. if we have needed = [1,2,0] this means that course 0 has 1
        un-met requirement, course 1 has 2 un-met requirements, and course 2 has 0 un-met requirements.
        '''
        dependencies = [[] for x in range(numCourses)]
        needed = [0 for x in range(numCourses)]
        
        for course, prereq in prerequisites:
            dependencies[prereq].append(course)
            needed[course] += 1

        # Retrieve available courses for initialization of BFS
        available = [i for i in range(numCourses) if needed[i] == 0]
        
        def BFS(graph, start, needed):
            queue, visited = start, set()
            
            while queue:
                vertex = queue.pop(0)
                if vertex not in visited:
                    visited.add(vertex)
                    for course in graph[vertex]:
                        needed[course] -= 1
                        if needed[course] == 0:
                            queue.append(course)
                    
            return visited
                
        visited = len(BFS(dependencies, available, needed))
        
        if visited == numCourses:
            return True
        else:
            return False
'''
This is also a solution to problem [210] Course Schedule II. We simply have to change visited to a list
and append each course we take. Then, we return the visited array if we are able to take all courses and 
return an empty array if we are not.
'''
