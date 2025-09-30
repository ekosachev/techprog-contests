class Solution:
    stack: list[int]

    def __init__(self):
        self.stack = [1, 1]

    def get_solution(self, n: int) -> int:
        while len(self.stack) < n:
            self.stack.append((self.stack[-1] + self.stack[-2]) % 10)
        return self.stack[n-1]

sol = Solution()
print(sol.get_solution(int(input())))
