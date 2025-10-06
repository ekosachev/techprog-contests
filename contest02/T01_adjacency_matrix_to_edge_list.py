class Solution:
    @classmethod
    def solve(cls, adjacency_matrix):
        for i, row in enumerate(adjacency_matrix, start=1):
            for j, is_connected in enumerate(row, start=1):
                if is_connected:
                    print(i, j)


n_verts: int = int(input())
adjacency_matrix: list[list[bool]] = []

for v in range(n_verts):
    adjacency_matrix.append(list(map(lambda x: bool(int(x)), input().split(" "))))

Solution.solve(adjacency_matrix)
