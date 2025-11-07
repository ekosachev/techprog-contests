from collections import defaultdict

class Solution:
    num_vert: int
    num_edge: int
    edges: list[tuple[int, int]] = []
    parent: list[int]
    rank: list[int]
    components: list[list[int]]

    def _find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self._find(self.parent[x])

        return self.parent[x]

    def _union(self, x: int, y: int) -> None:
        xr = self._find(x)
        yr = self._find(y)

        if xr == yr:
            return

        if self.rank[xr] < self.rank[yr]:
            self.parent[xr] = yr
        elif self.rank[xr] > self.rank[yr]:
            self.parent[yr] = xr
        else:
            self.parent[yr] = xr
            self.rank[xr] += 1

    def __init__(self, num_vert, num_edge, edges) -> None:
        self.num_vert = num_vert
        self.num_edge = num_edge
        self.edges = edges

        self.parent = list(range(self.num_vert))
        self.rank = [0] * self.num_vert
        self.components = [list() for _ in range(self.num_vert)]

    def solve(self) -> None:
        for u, v in self.edges:
            self._union(u, v)

        for i in range(self.num_vert):
            root = self._find(i)
            self.components[root].append(i)

num_vert, num_edge = tuple(map(int, input().split(' ')))
edges = [ tuple(map(lambda a: int(a) - 1, input().split(' '))) for _ in range(num_edge) ]
s = Solution(num_vert, num_edge, edges)
s.solve()
print(len([1 for component in s.components if component]))
for component in s.components:
    if not component:
        continue
    print(len(component))
    print(*map(lambda a: a + 1, component))

