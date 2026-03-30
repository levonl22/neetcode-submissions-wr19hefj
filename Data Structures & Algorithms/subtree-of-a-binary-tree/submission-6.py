# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        elif not subRoot or self.same(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def same(self, r, s):
        if not r and not s:
            return True
        elif not r or not s or r.val != s.val:
            return False
        
        return (self.same(r.left, s.left) and self.same(r.right, s.right))