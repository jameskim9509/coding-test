"""
여행 경로 재구성

항공권 목록 [출발지, 도착지]이 주어질 때, "JFK"에서 출발하는 여행 경로를 재구성하라.
여러 경로가 가능한 경우 사전순으로 가장 앞서는 경로를 반환하라.
모든 항공권은 반드시 한 번씩 사용해야 한다.

입력: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
출력: ["JFK","MUC","LHR","SFO","SJC"]
"""

import collections


def find_itinerary(tickets: list[list[str]]) -> list[str]:
    graph = collections.defaultdict(list)
    # pop()하기 위해서는 stack 구조로 넣어야하므로 역순 정렬
    for s, e in sorted(tickets, reverse=True):
        graph[s].append(e)

    result = []

    def dfs(node: str):
        # BFS로 순환 (top -> right -> left 방향이 존재할때 반영)
        while graph[node]:
            next_node = graph[node].pop()
            dfs(next_node)
        # 역순으로 result에 추가
        result.append(node)

    dfs("JFK")
    return result[::-1]


if __name__ == "__main__":
    tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(find_itinerary(tickets))
