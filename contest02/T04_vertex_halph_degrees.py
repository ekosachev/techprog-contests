class Solution:
    @classmethod
    def solve(cls):
        n_verts, n_edges = tuple(map(int, input().split(" ")))

        edges: list[list[int]] = []
        for _ in range(n_edges):
            edges.append(list(map(int, input().split(" "))))

        in_deg: list[int] = [0] * n_verts
        out_deg: list[int] = [0] * n_verts

        for edge in edges:
            from_v, to_v = edge[0], edge[1]
            in_deg[to_v - 1] += 1
            out_deg[from_v - 1] += 1

        for v in range(n_verts):
            print(in_deg[v])
            print(out_deg[v])


Solution.solve()
