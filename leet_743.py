"""
네트워크 딜레이 타임

n개의 노드로 이루어진 네트워크에서 times[i] = (u, v, w)는 노드 u에서 v로 가는 데 w만큼의 시간이 걸린다는 뜻이다.
노드 k에서 신호를 보낼 때, 모든 노드가 신호를 받는 데 걸리는 최소 시간을 반환하라.
모든 노드에 도달할 수 없으면 -1을 반환하라.

입력: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
출력: 2
"""

import collections
import heapq


def network_delay_time(times: list[list[int]], n: int, k: int) -> int:
    graph = collections.defaultdict(list)
    for time in times:
        graph[time[0]].append((time[1], time[2]))

    dist = collections.defaultdict(int)
    q = [(0, k)]
    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                w = w + time
                heapq.heappush(q, (w, v))

    if len(dist) == n:
        return max(dist.values())
    return -1


if __name__ == "__main__":
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    print(network_delay_time(times, n, k))
