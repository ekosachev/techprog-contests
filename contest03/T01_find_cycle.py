class Solution:
    def __init__(self, n: int, adjacency_matrix: list[list[int]]):
        self.n = n
        self.graph = adjacency_matrix
        self.visited = [False] * n
        self.parent = [-1] * n
        self.has_cycle = False
        self.cycle = []

    def solve(self):
        for start in range(self.n):
            if self.visited[start]:
                continue

            stack = [(start, -1)]
            self.parent[start] = -1

            while stack:
                u, parent = stack.pop()

                if not self.visited[u]:
                    self.visited[u] = True
                    self.parent[u] = parent

                    for v in range(self.n):
                        if self.graph[u][v] == 0:
                            continue

                        if not self.visited[v]:
                            stack.append((v, u))
                        elif v != parent:
                            self.has_cycle = True
                            self.cycle = self._reconstruct_cycle(u, v)
                            return

    def _reconstruct_cycle(self, u, v):
        path_u = [u]
        path_v = [v]

        while self.parent[u] != -1:
            u = self.parent[u]
            path_u.append(u)
            if u in path_v:
                break

        while self.parent[v] != -1:
            v = self.parent[v]
            path_v.append(v)
            if v in path_u:
                break

        meet = next(x for x in path_u if x in path_v)

        path_u = path_u[:path_u.index(meet) + 1]
        path_v = path_v[:path_v.index(meet)]
        path_v.reverse()
        return path_u + path_v


n = int(input())
adjacency_matrix = [list(map(int, input().split())) for _ in range(n)]

s = Solution(n, adjacency_matrix)
s.solve()
print("YES" if s.has_cycle else "NO")
if s.has_cycle:
	print(len(s.cycle))
	print(' '.join(map(lambda v: str(v + 1), s.cycle)))

