class Solution:
    def twoSum(self, numbers, target):
        left_pointer, right_pointer = 0, len(numbers) - 1

        while left_pointer < right_pointer:
            current_sum = numbers[left_pointer] + numbers[right_pointer]

            if current_sum == target:
                return [left_pointer + 1, right_pointer + 1]
            elif current_sum < target:
                left_pointer += 1
            else:
                right_pointer -= 1

        return []

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9),
        ([2, 3, 4], 6),
        ([-1, 0], -1),
        ([1, 2, 3, 4], 8)
    ]

    for numbers, target in test_cases:
        print(f"Numbers: {numbers}, Target: {target}, Result: {solution.twoSum(numbers, target)}")