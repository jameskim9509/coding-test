"""
키 순서로 대기열 재구성 (Queue Reconstruction by Height)

사람들이 뒤섞인 대기열이 있다. people[i] = [h_i, k_i]는 i번째 사람의 키가 h_i이고,
그 사람 앞에 키가 h_i 이상인 사람이 정확히 k_i명 서 있음을 뜻한다.
이 정보를 만족하도록 대기열을 재구성하여 반환하라.

입력: people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
출력: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

입력: people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
출력: [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]

입력: people = [[1, 0]]
출력: [[1, 0]]
"""


def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    sorted_people = sorted(people, key=lambda x: (-x[0], x[1]))
    result = []
    for elem in sorted_people:
        result.insert(elem[1], elem)
    return result


if __name__ == "__main__":
    print(reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(reconstruct_queue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
    print(reconstruct_queue([[1, 0]]))
