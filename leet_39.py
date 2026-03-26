"""
조합 합

서로 다른 양수로 이루어진 배열 candidates와 목표값 target이 주어질 때,
합이 target이 되는 모든 고유한 조합을 반환하라.
같은 숫자를 여러 번 선택할 수 있으며, 결과의 순서는 상관없다.

입력: candidates = [2, 3, 6, 7], target = 7
출력: [[2, 2, 3], [7]]
"""


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    results = []

    def dfs(ind: int, candidates: list[int], result: list[int]):
        if sum(result) == target:
            results.append(result.copy())
            return

        if sum(result) > target:
            return

        for i in range(ind, len(candidates)):
            result.append(candidates[i])
            dfs(i, candidates, result)
            result.pop()

    dfs(0, candidates, [])
    return results


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7
    print(combination_sum(candidates, target))
