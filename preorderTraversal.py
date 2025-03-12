# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        self.pre_traversal(root, result)
        return result
    def pre_traversal(self, node: TreeNode, result: List[int]):
        if node:
            result.append(node.val)
            self.pre_traversal(node.left, result)
            self.pre_traversal(node.right, result)