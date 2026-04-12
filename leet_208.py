"""
트라이 구현 (Implement Trie - Prefix Tree)

트라이(Trie) 또는 접두사 트리는 문자열 집합에서 키를 효율적으로 저장하고 검색하는 데 사용되는 트리 자료구조이다.
이 자료구조는 자동완성, 맞춤법 검사 등 다양한 응용 분야가 있다.

Trie 클래스를 구현하라:
- Trie(): 트라이 객체를 초기화한다.
- void insert(String word): 문자열 word를 트라이에 삽입한다.
- boolean search(String word): 문자열 word가 트라이에 있으면(즉, 이전에 삽입되었으면) true를, 그렇지 않으면 false를 반환한다.
- boolean startsWith(String prefix): 이전에 삽입된 문자열 중 접두사가 prefix인 것이 있으면 true를, 그렇지 않으면 false를 반환한다.

입력:
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
출력:
[null, null, true, false, true, null, true]
"""

import collections


class Node:
    def __init__(self):
        self.children: dict[str, Node] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]

        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]

        if not node.is_end:
            return False

        return True

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))  # True
    print(trie.search("app"))  # False
    print(trie.starts_with("app"))  # True
    trie.insert("app")
    print(trie.search("app"))  # True
