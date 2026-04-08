"""
이진 탐색 트리의 범위 합 (Range Sum of BST)

이진 탐색 트리의 루트 root와 두 정수 low, high가 주어질 때,
값이 [low, high] 범위에 속하는 모든 노드의 값의 합을 반환하라.

입력: root = [10, 5, 15, 3, 7, null, 18], low = 7, high = 15
출력: 32

입력: root = [10, 5, 15, 3, 7, 13, 18, 1, null, 6], low = 6, high = 10
출력: 23
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def range_sum_bst(root: TreeNode | None, low: int, high: int) -> int:
    result = 0

    def dfs(node: TreeNode | None):
        nonlocal result
        if node is None:
            return

        if low <= node.val and node.val <= high:
            result += node.val
            dfs(node.left)
            dfs(node.right)

        if node.val < low:
            dfs(node.right)

        if node.val > high:
            dfs(node.left)

    dfs(root)

    return result


if __name__ == "__main__":
    root = TreeNode(
        10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))
    )
    print(range_sum_bst(root, 7, 15))
