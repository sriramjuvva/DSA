# Definition for a binary tree node.
class TreeNode:
    def __init__(self, root=0, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

class Solution:
    def invertTree(self,root):
        if not root:
            return 
        stack = [root]
        while stack:
            node = stack.pop()
            node.left , node.right = node.right , node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return self.root
        
a = TreeNode(root= 5,left=8,right=9)
print(a.invertTree(root=5))
        