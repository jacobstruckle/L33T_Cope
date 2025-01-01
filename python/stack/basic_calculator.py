class Solution:
    def calculate(self, expression: str) -> int:
        def evaluate_expression(tokens):
            stack = []
            num = 0
            sign = 1
            result = 0

            for char in tokens:
                if char.isdigit():
                    num = num * 10 + int(char)
                elif char in "+-":
                    result += sign * num
                    num = 0
                    sign = 1 if char == "+" else -1
                elif char == "(":
                    stack.append((result, sign))
                    result, sign = 0, 1
                elif char == ")":
                    result += sign * num
                    num = 0
                    last_result, last_sign = stack.pop()
                    result = last_result + last_sign * result

            result += sign * num
            return result

        sanitized_expression = expression.replace(" ", "")
        return evaluate_expression(sanitized_expression)

solver = Solution()
print(solver.calculate("1 + 1")) 
print(solver.calculate(" 2-1 + 2 "))
print(solver.calculate("(1+(4+5+2)-3)+(6+8)"))
