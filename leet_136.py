"""
싱글 넘버 (Single Number)

비어있지 않은 정수 배열 nums가 주어졌을 때, 모든 원소는 두 번씩 나타나지만
오직 한 원소만 한 번 나타난다. 그 원소를 찾아 반환하라.
시간복잡도는 O(n), 추가 공간은 상수만 사용해야 한다.

입력: nums = [2, 2, 1]
출력: 1

입력: nums = [4, 1, 2, 1, 2]
출력: 4

입력: nums = [1]
출력: 1
"""


def single_number(nums: list[int]) -> int:
    result = 0
    for num in nums:
        result ^= num
    return result


if __name__ == "__main__":
    print(single_number([2, 2, 1]))
    print(single_number([4, 1, 2, 1, 2]))
    print(single_number([1]))
