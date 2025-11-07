from collections import defaultdict
import heapq

vertex = int
weight = float


class Solution:
    n_v: int

    @classmethod
    def dijkstra(cls, n_v: int, adjacency_matrix: list[list[int]], start: vertex) -> list[weight]:

        adjacency_list: dict[vertex, list[tuple[vertex, weight]]] = defaultdict(list)
        
        for u, row in enumerate(adjacency_matrix):
            for v, w in enumerate(row):
                if w <= 0:
                    continue
                adjacency_list[u].append((v, float(w)))

        dist: list[weight] = [float('inf')] * n_v
        dist[start] = 0

        pq: list[tuple[weight, vertex]] = [(0, start)]

        while pq:
            current_dist, u = heapq.heappop(pq)

            if current_dist > dist[u]:
                continue

            for v, w in adjacency_list[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))

        return dist


if __name__ == "__main__":
    n, s, f = tuple(map(int, input().split()))
    adjacency_matrix = [ list(map(int, input().split())) for _ in range(n) ]
    
    s -= 1
    f -= 1

    dist = Solution.dijkstra(n, adjacency_matrix, s)
    print(int(dist[f]) if dist[f] != float('inf') else -1)
