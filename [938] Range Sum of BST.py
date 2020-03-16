Problem:
'''
Given the root node of a binary search tree, return the sum of values of all nodes with 
value between L and R (inclusive).

The binary search tree is guaranteed to have unique values.

Example - 
Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
Output: 32
'''

# Solution: (Faster than 40.75% of all python3 submissions) - Can be improved further.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def __init__(self):
        self.sum_ = 0
    
    def sumBetween(self, node, L, R):
        if node.val <= R and node.val >= L:
            self.sum_ += node.val
        if node.left:
            self.sumBetween(node.left, L, R)
        if node.right:
            self.sumBetween(node.right, L, R)
        return self.sum_
    
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        return self.sumBetween(root, L, R)
