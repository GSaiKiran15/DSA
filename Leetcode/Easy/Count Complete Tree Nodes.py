# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def countNodes(self, root) -> int:
        count = 0
        stack = [root]
        if root is None:
            return 0
        while stack:
            root = stack.pop(-1)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            count += 1
        return count
            