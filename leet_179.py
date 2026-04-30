"""
가장 큰 수 (Largest Number)

음이 아닌 정수 배열 nums가 주어졌을 때, 이들을 이어붙여 만들 수 있는 가장 큰 수를
문자열로 반환하라.

입력: nums = [10, 2]
출력: "210"

입력: nums = [3, 30, 34, 5, 9]
출력: "9534330"

입력: nums = [0, 0]
출력: "0"
"""

from functools import cmp_to_key


def largest_number(nums: list[int]) -> str:
    nums.sort(key=cmp_to_key(lambda a, b: int(str(b) + str(a)) - int(str(a) + str(b))))
    return "0" if nums[0] == 0 else "".join(map(str, nums))


if __name__ == "__main__":
    print(largest_number([10, 2]))
    print(largest_number([3, 30, 34, 5, 9]))
    print(largest_number([0, 0]))
