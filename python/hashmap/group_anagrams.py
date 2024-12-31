from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        anagram_groups = defaultdict(list)
        
        for string in strs:
            sorted_key = ''.join(sorted(string))
            anagram_groups[sorted_key].append(string)
        
        return list(anagram_groups.values())      