"""
섬의 개수

입력: [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]
출력: 1
"""


def find_island(i: int, j: int, visited: list[list]):
    if i >= len(visited) or j >= len(visited[0]) or visited[i][j]:
        return

    visited[i][j] = True
    find_island(i + 1, j, visited)
    find_island(i, j + 1, visited)


def count_islands(input_lists: list[list]) -> int:
    visited = [[False] * len(input_lists[0])] * len(input_lists)
    count = 0
    for i, lst in enumerate(visited):
        for j, is_visited in enumerate(lst):
            if is_visited is False:
                find_island(i, j, visited)
                count += 1

    return count


if __name__ == "__main__":
    input_lists = [[1, 1, 1, 1, 0], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]]
    print(count_islands(input_lists=input_lists))
