"""
원점에 K번째로 가까운 점들 (K Closest Points to Origin)

X-Y 평면 위의 점들의 배열 points와 정수 k가 주어졌을 때, 원점 (0, 0)에서 가장 가까운
k개의 점을 반환하라. 두 점 사이의 거리는 유클리드 거리이며, 답의 순서는 상관없다.

입력: points = [[1, 3], [-2, 2]], k = 1
출력: [[-2, 2]]

입력: points = [[3, 3], [5, -1], [-2, 4]], k = 2
출력: [[3, 3], [-2, 4]]

입력: points = [[0, 1], [1, 0]], k = 2
출력: [[0, 1], [1, 0]]
"""

import heapq


def k_closest(points: list[list[int]], k: int) -> list[list[int]]:
    heap = []
    for point in points:
        dist = point[0] * point[0] + point[1] * point[1]
        heapq.heappush(heap, (dist, point))

    result = []
    for _ in range(k):
        _, point = heapq.heappop(heap)
        result.append(point)
    return result


if __name__ == "__main__":
    print(k_closest([[1, 3], [-2, 2]], 1))
    print(k_closest([[3, 3], [5, -1], [-2, 4]], 2))
    print(k_closest([[0, 1], [1, 0]], 2))
