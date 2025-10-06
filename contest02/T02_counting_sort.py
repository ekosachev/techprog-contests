class Solution:
    @classmethod
    def solve(cls, n: int, sequence: list[int]) -> None:
        counters: list[int] = [0] * 10
        sorted_sequence: list[int] = []

        for i in range(n):
            element = sequence.pop(0)
            counters[element - 1] += 1

        for i in range(10):
            for _ in range(counters[i]):
                sorted_sequence.append(i + 1)

        print(" ".join(map(str, sorted_sequence)))


n = int(input())
seq = list(map(int, input().split(" ")))
Solution.solve(n, seq)
