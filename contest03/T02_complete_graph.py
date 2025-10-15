class Solution:
    edge_list: list[tuple[int, int]]
    n: int
    m: int
    connectivity_matrix: list[list[int]]
    is_complete: bool = False

    def __init__(self, n: int, m: int, edge_list: list[tuple[int, int]]):
        self.n = n
        self.m = m
        self.edge_list = edge_list
        self.connectivity_matrix = [[0] * n for _ in range(n)] 

    def solve(self):
        for v in range(self.n):
            self.connectivity_matrix[v][v] = 1
        for u, v in self.edge_list:
            self.connectivity_matrix[u - 1][v - 1] = 1
            self.connectivity_matrix[v - 1][u - 1] = 1


        if all(all(row) for row in self.connectivity_matrix):
            self.is_complete = True

n, m = tuple(map(int, input().split(" ")))
edge_list = [tuple(map(int, input().split(" "))) for _ in range(m)]
s = Solution(n, m, edge_list)
s.solve()
print("YES" if s.is_complete else "NO")
