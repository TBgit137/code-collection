# 二叉树中是否存在一条从根节点到叶子节点的路径，使得路径上所有节点值的和等于给定的目标和
# 递归，每递归一次就减一次值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def has_path_sum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False

        targetSum -= root.val

        if root.left is None and root.right is None:
            return targetSum == 0

        return (self.hasPathSum(root.left, targetSum)) or (self.hasPathSum(root.right, targetSum))