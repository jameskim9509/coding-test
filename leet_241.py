"""
괄호를 추가하는 다양한 방법 (Different Ways to Add Parentheses)

숫자와 연산자 +, -, * 로 이루어진 문자열 expression이 주어진다.
숫자와 연산자를 괄호로 그룹 짓는 모든 가능한 방법에 대해 계산한 결과를
모두 담은 리스트를 반환하라. 결과의 순서는 상관없다.
예를 들어 "2-1-1"은 ((2-1)-1) = 0, (2-(1-1)) = 2 두 가지로 그룹 지을 수 있다.

입력: expression = "2-1-1"
출력: [0, 2]

입력: expression = "2*3-4*5"
출력: [-34, -14, -10, -10, 10]
"""

def diff_ways_to_compute(expression: str) -> list[int]:
    def compute(left, right, op):
        result = []
        for l in left:
            for r in right:
                result.append(
                    eval(str(l) + op + str(r))
                )
        
        return result

    if expression.isdigit():
        return [int(expression)]

    rs = []
    for i, ch in enumerate(expression):
        if ch in "+*-":
            left = diff_ways_to_compute(expression[:i])
            right = diff_ways_to_compute(expression[i+1:])
            rs.extend(compute(left, right, ch))
    return rs


if __name__ == "__main__":
    print(diff_ways_to_compute("2-1-1"))  # [0, 2]
    print(diff_ways_to_compute("2*3-4*5"))  # [-34, -14, -10, -10, 10]
