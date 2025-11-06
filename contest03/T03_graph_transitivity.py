class Solution:
    n: int
    adjacency_matrix: list[list[int]]
    is_transitive: bool = True

    def __init__(self, n, adjacency_matrix: list[list[int]]):
        self.n = n
        self.adjacency_matrix = adjacency_matrix

    def solve(self):
        for u in range(self.n):
            for v in range(self.n):
                if self.adjacency_matrix[u][v]:
                    for w in range(self.n):
                        # если u->v и v->w, то должно быть u->w
                        if self.adjacency_matrix[v][w] and not self.adjacency_matrix[u][w]:
                            self.is_transitive = False
                            return

n = int(input())
adjacency_matrix = [list(map(int, input().split(" "))) for _ in range(n)]
s = Solution(n, adjacency_matrix)
s.solve()
print("YES" if s.is_transitive else "NO")


