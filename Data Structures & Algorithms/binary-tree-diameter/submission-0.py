# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def ht_of_tree(root: Optional[TreeNode]):
            if not root:
                return 0
            
            left = ht_of_tree(root.left)
            right = ht_of_tree(root.right)

            return max(left, right) + 1
        
        def diam(root: Optional[TreeNode]):
            if not root:
                return 0
            
            left_diam = diam(root.left)
            right_diam = diam(root.right)

            d = ht_of_tree(root.left) + ht_of_tree(root.right)

            return max(left_diam, right_diam, d)
        
        return diam(root)