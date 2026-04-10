"""
배열에서 K번째로 큰 요소 (Kth Largest Element in an Array)

정수 배열 nums와 정수 k가 주어질 때,
배열에서 k번째로 큰 요소를 반환하라.
정렬된 순서에서 k번째로 큰 요소이지, k번째로 구별되는 요소가 아님에 유의하라.

입력: nums = [3, 2, 1, 5, 6, 4], k = 2
출력: 5

입력: nums = [3, 2, 3, 1, 2, 4, 5, 5, 6], k = 4
출력: 4
"""

import heapq


def find_kth_largest(nums: list[int], k: int) -> int:
    heap = []
    while nums:
        val = nums.pop()
        heapq.heappush(heap, val)
        if len(heap) > k:
            heapq.heappop(heap)

    return heapq.heappop(heap)


if __name__ == "__main__":
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
