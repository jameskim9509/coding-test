"""
정렬된 배열에서 두 수의 합 (Two Sum II - Input Array Is Sorted)

오름차순으로 정렬된 1-indexed 정수 배열 numbers와 정수 target이 주어졌을 때,
두 수를 더해 target이 되는 인덱스 쌍 [i, j] (1 <= i < j)를 반환하라.
정답은 유일하며, 같은 원소를 두 번 사용할 수 없다. 추가 공간은 상수만 사용해야 한다.

입력: numbers = [2, 7, 11, 15], target = 9
출력: [1, 2]

입력: numbers = [2, 3, 4], target = 6
출력: [1, 3]

입력: numbers = [-1, 0], target = -1
출력: [1, 2]
"""


def two_sum(numbers: list[int], target: int) -> list[int]:
    def find_number(numbers, number, start):
        left, right = start, len(numbers) - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] < number:
                left = mid + 1
            elif numbers[mid] > number:
                right = mid - 1
            else:
                return mid
        return -1

    for i, number in enumerate(numbers):
        target_index = find_number(numbers, target - number, i + 1)
        if target_index != -1:
            return [i + 1, target_index + 1]


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))
    print(two_sum([2, 3, 4], 6))
    print(two_sum([-1, 0], -1))
