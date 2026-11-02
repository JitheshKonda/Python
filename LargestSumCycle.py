class Solution:
    def largestSumCycle(self, edge: list[int]) -> int:
        n = len(edge)
        visited = [0] * n
        max_sum = -1

        for i in range(n):
            if visited[i]:
                continue

            curr = i
            dist = {}
            d = 0

            while curr != -1:
                if visited[curr] == 1:
                 
                    break
                if curr in dist:
                    cycle_sum = d - dist[curr]
                    max_sum = max(max_sum, cycle_sum)
                    break

                dist[curr] = d
                d += curr
                curr = edge[curr]

            curr = i
            while curr != -1 and visited[curr] == 0:
                visited[curr] = 1
                curr = edge[curr]

        return max_sum
