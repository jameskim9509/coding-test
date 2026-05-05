"""
회전된 정렬된 배열에서 검색 (Search in Rotated Sorted Array)

오름차순으로 정렬된 후 알 수 없는 지점에서 회전된 정수 배열 nums와 정수 target이
주어졌을 때, target의 인덱스를 반환하라. 없으면 -1을 반환한다.
시간복잡도는 O(log n) 이어야 한다.

입력: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
출력: 4

입력: nums = [4, 5, 6, 7, 0, 1, 2], target = 3
출력: -1

입력: nums = [1], target = 0
출력: -1
"""


def search(nums: list[int], target: int) -> int:
    def find_pivot(nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return left

    def find_target(nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    pivot = find_pivot(nums=nums)
    if pivot == -1:
        return find_target(nums=nums, target=target)

    left_nums = nums[:pivot]
    right_nums = nums[pivot:]

    result = find_target(nums=left_nums, target=target)
    if result != -1:
        return result
    right_result = find_target(nums=right_nums, target=target)
    if right_result == -1:
        return -1
    return pivot + right_result


if __name__ == "__main__":
    print(search([4, 5, 6, 7, 0, 1, 2], 0))
    print(search([4, 5, 6, 7, 0, 1, 2], 3))
    print(search([1], 0))
