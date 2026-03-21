"""
중복 문자 없는 가장 긴 부분 문자열

입력: "abcabcbb"
출력: 3
"""


def cal_len_of_longest_string_without_duplication(input_str: str) -> int:
    max_cnt, start_ind = 0, 0
    while start_ind < len(input_str):
        cnt = 0
        idx_map = {}
        for ind in range(start_ind, len(input_str)):
            ch = input_str[ind]
            if ch in idx_map:
                start_ind = idx_map[ch] + 1
                max_cnt = cnt if max_cnt < cnt else max_cnt
                break

            idx_map[ch] = ind
            cnt += 1
        if ind == len(input_str) - 1:
            max_cnt = cnt if max_cnt < cnt else max_cnt
            break
    return max_cnt


if __name__ == "__main__":
    INPUT_STR = "abcabcbb"
    print(cal_len_of_longest_string_without_duplication(INPUT_STR))
