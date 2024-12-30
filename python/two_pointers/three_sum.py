class Solution:
    def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left_pointer, right_pointer = i + 1, len(nums) - 1

            while left_pointer < right_pointer:
                current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]

                if current_sum == 0:
                    result.append([nums[i], nums[left_pointer], nums[right_pointer]])

                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer + 1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer - 1]:
                        right_pointer -= 1

                    left_pointer += 1
                    right_pointer -= 1
                elif current_sum < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        return result

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        [-1, 0, 1, 2, -1, -4],
        [0, 0, 0, 0],
        [], 
        [1, 2, -2, -1]
    ]

    for nums in test_cases:
        print(f"Input: {nums}, Triplets: {solution.threeSum(nums)}")