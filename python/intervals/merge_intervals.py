class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda interval: interval[0])

        merged_intervals = []

        for interval in intervals:
            if not merged_intervals or merged_intervals[-1][1] < interval[0]:
                merged_intervals.append(interval)
            else:
                merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

        return merged_intervals
