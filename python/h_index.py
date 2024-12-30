class Solution:
    def hIndex(self, citations):
        sorted_citations = sorted(citations, reverse=True)        
        h_index = 0
        for i, citation_count in enumerate(sorted_citations):
            if citation_count >= i + 1:
                h_index = i + 1
            else:
                break        
        return h_index
solution = Solution()
print(solution.hIndex([3, 0, 6, 1, 5]))
print(solution.hIndex([1, 3, 1]))