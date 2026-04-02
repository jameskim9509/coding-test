"""
이진 트리의 최대 깊이

이진 트리의 루트가 주어질 때, 최대 깊이를 반환하라.
최대 깊이는 루트 노드에서 가장 먼 리프 노드까지의 경로에 있는 노드의 수이다.

입력: root = [3, 9, 20, null, null, 15, 7]
출력: 3
"""

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    if not root:
        return 0

    dq = collections.deque([root])
    depth = 0
    while dq:
        depth += 1
        for _ in range(len(dq)):
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
    return depth


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(max_depth(root))
