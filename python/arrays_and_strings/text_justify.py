class Solution:
    def fullJustify(self, words, max_width):
        result = []
        current_line = []
        current_line_length = 0

        for word in words:
            if current_line_length + len(word) + len(current_line) > max_width:
                for i in range(max_width - current_line_length):
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                result.append(''.join(current_line))
                current_line = []
                current_line_length = 0

            current_line.append(word)
            current_line_length += len(word)

        last_line = ' '.join(current_line).ljust(max_width)
        result.append(last_line)

        return result

words1 = ["This", "is", "an", "example", "of", "text", "justification."]
max_width1 = 16

words2 = ["What","must","be","acknowledgment","shall","be"]
max_width2 = 16

words3 = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
max_width3 = 20

solution = Solution()
print(solution.fullJustify(words1, max_width1))
print(solution.fullJustify(words2, max_width2))
print(solution.fullJustify(words3, max_width3))
