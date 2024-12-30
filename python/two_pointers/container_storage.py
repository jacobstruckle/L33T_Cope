class Solution:
    def maxArea(self, heights):
        left_pointer, right_pointer = 0, len(heights) - 1
        max_area = 0

        while left_pointer < right_pointer:

            container_height = min(heights[left_pointer], heights[right_pointer])
            container_width = right_pointer - left_pointer

            current_area = container_height * container_width
            max_area = max(max_area, current_area)

            if heights[left_pointer] < heights[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [1, 8, 6, 2, 5, 4, 8, 3, 7],
        [1, 1],
        [4, 3, 2, 1, 4],
        [1, 2, 1]
    ]

    for heights in test_cases:
        print(f"Heights: {heights}, Max Area: {solution.maxArea(heights)}")
