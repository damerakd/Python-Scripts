# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        max_num = max(nums)
        root = TreeNode(max_num)
        index = nums.index(max_num)        
        if len(nums[:index]):
            root.left = self.constructMaximumBinaryTree(nums[:index])
        if len(nums[index+1:]):
            root.right= self.constructMaximumBinaryTree(nums[index+1:])        
        return root