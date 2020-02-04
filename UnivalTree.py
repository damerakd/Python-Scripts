# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return True
        if root.left != None and root.val != root.left.val:
            return False
        if root.right != None and root.val != root.right.val:
            return False
        if self.isUnivalTree(root.left) and self.isUnivalTree(root.right):
            return True
        return False