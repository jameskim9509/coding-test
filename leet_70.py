"""
계단 오르기 (Climbing Stairs)

꼭대기까지 n개의 계단을 올라야 한다. 한 번에 1칸 또는 2칸씩 오를 수 있을 때,
꼭대기에 도달하는 서로 다른 방법의 수를 반환하라.

입력: n = 2
출력: 2
설명: (1칸 + 1칸), (2칸)

입력: n = 3
출력: 3
설명: (1+1+1), (1+2), (2+1)

입력: n = 5
출력: 8
"""
import collections


dp = collections.defaultdict(int)
dp[1] = 1
dp[2] = 2

def climb_stairs(n: int) -> int:
    if dp[n]:
        return dp[n]
    
    dp[n] = climb_stairs(n-1) + climb_stairs(n-2)
    return dp[n]


if __name__ == "__main__":
    print(climb_stairs(2))  # 2
    print(climb_stairs(3))  # 3
    print(climb_stairs(5))  # 8
