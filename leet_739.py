"""
일일 온도 - 따뜻한 날씨를 위해 기다려야 하는 시간
입력: [73, 74, 75, 71, 69, 72, 76, 73]
출력: [1, 1, 4, 2, 1, 1, 0, 0]
"""


def calculate_day_for_warm(inputs: list):
    """
    따뜻해지기 위한 날짜 계산 함수
    """
    ans = [0] * len(inputs)
    st = []
    for ind, val in enumerate(inputs):
        while len(st) > 0 and inputs[st[-1]] < val:
            ans_ind = st.pop()
            ans[ans_ind] = ind - ans_ind
        st.append(ind)
    return ans


if __name__ == "__main__":
    input_list = [73, 74, 75, 71, 69, 72, 76, 73]
    outpust_list = calculate_day_for_warm(input_list)
    print(outpust_list)
