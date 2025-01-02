from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional['TreeNode']) -> int:
        self.max_sum = float('-inf')

        def calculate_max_gain(node: Optional['TreeNode']) -> int:
            if not node:
                return 0

            left_gain = max(calculate_max_gain(node.left), 0)
            right_gain = max(calculate_max_gain(node.right), 0)

            current_path_sum = node.val + left_gain + right_gain

            self.max_sum = max(self.max_sum, current_path_sum)

            return node.val + max(left_gain, right_gain)

        calculate_max_gain(root)
        return self.max_sum

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
solution = Solution()
print(solution.maxPathSum(root))

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(solution.maxPathSum(root))   