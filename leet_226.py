"""
이진 트리 반전 (Invert Binary Tree)

이진 트리의 루트가 주어질 때, 트리를 반전시키고 루트를 반환하라.

입력: root = [4, 2, 7, 1, 3, 6, 9]
출력: [4, 7, 2, 9, 6, 3, 1]
"""

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    q = collections.deque([root])
    while q:
        node = q.popleft()
        node.left, node.right = node.right, node.left

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

    return root


if __name__ == "__main__":
    root = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    result = invert_tree(root)
