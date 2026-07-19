"""
다수 원소 (Majority Element)

크기 n인 배열 nums가 주어졌을 때, 다수 원소를 반환하라.
다수 원소는 n // 2번보다 많이 등장하는 원소이며, 항상 존재한다고 가정한다.

입력: nums = [3, 2, 3]
출력: 3

입력: nums = [2, 2, 1, 1, 1, 2, 2]
출력: 2

입력: nums = [1]
출력: 1
"""


def majority_element(nums: list[int]) -> int:
    def find_majority(start, end) -> int:
        if start == end: 
            return nums[start]

        mid = (start + end) // 2
        left_cand = find_majority(start, mid)
        right_cand = find_majority(mid+1, end)
        
        if left_cand == right_cand:
            return left_cand
    
        left_cand_count = sum(1 for i in range(start, end + 1) if nums[i] == left_cand)
        left_right_count = sum(1 for i in range(start, end + 1) if nums[i] == right_cand)
        return left_cand if left_cand_count > left_right_count else right_cand
    return find_majority(0, len(nums)-1)


if __name__ == "__main__":
    print(majority_element([3, 2, 3]))
    print(majority_element([2, 2, 1, 1, 1, 2, 2]))
    print(majority_element([1]))
