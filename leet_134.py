"""
주유소 (Gas Station)

원형 경로를 따라 n개의 주유소가 있고, i번째 주유소의 기름 양은 gas[i]이다.
자동차의 연료 탱크는 무제한이며, i번째 주유소에서 다음 (i+1)번째 주유소로
이동하는 데 cost[i]만큼의 기름이 든다. 빈 탱크로 어느 한 주유소에서 출발한다.
두 정수 배열 gas와 cost가 주어질 때, 시계 방향으로 경로를 한 바퀴 돌 수 있으면
출발 주유소의 인덱스를 반환하고, 불가능하면 -1을 반환하라.
해가 존재한다면 그 해는 유일함이 보장된다.

입력: gas = [1, 2, 3, 4, 5], cost = [3, 4, 5, 1, 2]
출력: 3

입력: gas = [2, 3, 4], cost = [3, 4, 3]
출력: -1
"""


def can_complete_circuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost): return -1

    start, fuel = 0, 0
    for i, g in enumerate(gas):
        if g + fuel >= cost[i]:
            fuel += (g - cost[i])
        else:
            start = i + 1
            fuel = 0
    return start


if __name__ == "__main__":
    print(can_complete_circuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))  # 3
    print(can_complete_circuit([2, 3, 4], [3, 4, 3]))  # -1
