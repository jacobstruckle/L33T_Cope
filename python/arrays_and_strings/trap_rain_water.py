class Solution:
    def trap(self, height):
        if not height or len(height) < 3:
            return 0

        total_water = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(len(height)):
            trapped_water_at_position = min(left_max[i], right_max[i]) - height[i]
            total_water += trapped_water_at_position

        return total_water

solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(solution.trap([4,2,0,3,2,5]))