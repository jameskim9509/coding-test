"""
k개 정렬 리스트 병합

입력: [[1, 4, 5], [1, 3, 4], [2, 6]]
출력: [1, 1, 2, 3, 4, 4, 5, 6]
"""

import heapq


def merge_k_lists(lists: list[list]):
    """
    k개 정렬 리스트를 받아 하나의 정렬 리스트로 변환
    """
    heap = []
    for lst in lists:
        for idx, val in enumerate(lst):
            heapq.heappush(heap, (val, idx, lst))

    result = []
    while heap:
        node = heapq.heappop(heap)
        result.append(node[0])

    return result


if __name__ == "__main__":
    input_list = [[1, 4, 5], [1, 3, 4], [2, 6]]
    print(merge_k_lists(input_list))
