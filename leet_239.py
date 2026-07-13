"""
슬라이딩 윈도우 최댓값 (Sliding Window Maximum)

정수 배열 nums와 정수 k가 주어진다. 크기가 k인 슬라이딩 윈도우가 배열의 가장 왼쪽에서
가장 오른쪽으로 이동한다. 윈도우 안의 k개 숫자만 볼 수 있으며, 윈도우는 매번 오른쪽으로
한 칸씩 이동한다. 각 윈도우에서의 최댓값을 배열로 반환하라.

입력: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
출력: [3, 3, 5, 5, 6, 7]

입력: nums = [1], k = 1
출력: [1]

입력: nums = [9, 8, 7, 6], k = 2
출력: [9, 8, 7]
"""

import collections


def max_sliding_window(nums: list[int], k: int) -> list[int]:
    dq = collections.deque([])
    rs = []
    for i, v in enumerate(nums):
        # deque에 k개 이상 쌓여있을 경우 왼쪽에서부터 제거
        if dq and i - dq[0][0] >= k:
            dq.popleft()
      
        # deque의 가장 오른쪽(최소값) 데이터보다 넣을 데이터가 클 경우 제거
        # 항상 가장 오른쪽 값이 최솟값을 유지하면서 최대 인덱스를 유지
        while dq and dq[-1][1] < v:
            dq.pop()
        
        dq.append((i, v))
        
        if i >= k-1:
            rs.append(dq[0][1])
    
    return rs



if __name__ == "__main__":
    print(max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
    print(max_sliding_window([1], 1))  # [1]
    print(max_sliding_window([9, 8, 7, 6], 2))  # [9, 8, 7]
