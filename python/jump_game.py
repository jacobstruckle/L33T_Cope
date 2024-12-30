class Solution:
    def canJump(self, nums):
        max_reachable_index = 0
        for current_index, jump_length in enumerate(nums):
            if current_index > max_reachable_index:
                return False
            max_reachable_index = max(max_reachable_index, current_index + jump_length)
            if max_reachable_index >= len(nums) - 1:
                return True
        return False
solution = Solution()
print(solution.canJump([2, 3, 1, 1, 4]))
print(solution.canJump([3, 2, 1, 0, 4]))