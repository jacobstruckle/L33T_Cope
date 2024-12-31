class Solution:
    def insert(self, intervals, new_interval):
        merged_intervals = []
        i = 0
        n = len(intervals)

        while i < n and intervals[i][1] < new_interval[0]:
            merged_intervals.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1
        merged_intervals.append(new_interval)

        while i < n:
            merged_intervals.append(intervals[i])
            i += 1

        return merged_intervals

solution = Solution()

intervals1 = [[1, 3], [6, 9]]
new_interval1 = [2, 5]
print(solution.insert(intervals1, new_interval1))

intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval2 = [4, 8]
print(solution.insert(intervals2, new_interval2))