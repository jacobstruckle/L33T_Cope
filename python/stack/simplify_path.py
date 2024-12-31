class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = [part for part in path.split('/') if part not in ['', '.']]
        
        stack = []

        for part in parts:
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        simplified_path = "/" + "/".join(stack)
        
        return simplified_path

if __name__ == "__main__":
    solution = Solution()

    # Test cases
    print(solution.simplifyPath("/home/"))  # Output: "/home"
    print(solution.simplifyPath("/home//foo/"))  # Output: "/home/foo"
    print(solution.simplifyPath("/home/user/Documents/../Pictures"))  # Output: "/home/user/Pictures"
    print(solution.simplifyPath("/../"))  # Output: "/"
    print(solution.simplifyPath("/.../a/../b/c/../d/./"))  # Output: "/.../b/d"