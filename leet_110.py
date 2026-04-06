"""
균형 이진 트리 (Balanced Binary Tree)

이진 트리의 루트가 주어질 때, 트리가 높이 균형인지 판별하라.
높이 균형 이진 트리란 모든 노드의 왼쪽과 오른쪽 서브트리의 높이 차이가 1 이하인 트리이다.

입력: root = [3, 9, 20, null, null, 15, 7]
출력: true

입력: root = [1, 2, 2, 3, 3, null, null, 4, 4]
출력: false
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_balanced(root: TreeNode | None) -> bool:
    result = True

    def max_depth(node: TreeNode | None) -> int:
        nonlocal result
        if node is None:
            return 0

        left_depth = max_depth(node.left) + 1
        right_depth = max_depth(node.right) + 1
        if abs(left_depth - right_depth) > 1:
            result = False

        return max(left_depth, right_depth)

    max_depth(root)
    return result


if __name__ == "__main__":
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(is_balanced(root))
