"""
순열

서로 다른 정수로 이루어진 배열이 주어질 때, 가능한 모든 순열을 반환하라.

입력: [1, 2, 3]
출력: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""


def permute(nums: list[int]) -> list[list[int]]:
    results = []

    def dfs(nums, visited, result: list):
        if len(result) == len(nums):
            results.append(result.copy())
            return

        for i, v in enumerate(nums):
            if visited[i]:
                continue

            result.append(v)
            visited[i] = True
            dfs(nums, visited, result)
            result.pop()
            visited[i] = False

    visited = [False] * len(nums)
    dfs(nums, visited, [])
    return results


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(permute(nums))
