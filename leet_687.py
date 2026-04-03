"""
가장 긴 같은 값 경로 (Longest Univalue Path)

이진 트리의 루트가 주어질 때, 같은 값을 가진 노드로 이루어진 가장 긴 경로의 길이를 반환하라.
경로의 길이는 경로에 있는 간선(edge)의 수로 측정된다.

입력: root = [5, 4, 5, 1, 1, null, 5]
출력: 2

입력: root = [1, 4, 5, 4, 4, null, 5]
출력: 2
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_univalue_path(root: TreeNode | None) -> int:
    result = 0

    def dfs(node: TreeNode):
        nonlocal result
        if node is None:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        left_path = 0
        if node.left and node.left.val == node.val:
            left_path = left + 1

        right_path = 0
        if node.right and node.right.val == node.val:
            right_path = right + 1

        result = max(result, left_path + right_path)
        return max(left_path, right_path)

    dfs(root)
    return result


if __name__ == "__main__":
    root = TreeNode(
        5, TreeNode(4, TreeNode(1), TreeNode(1)), TreeNode(5, None, TreeNode(5))
    )
    print(longest_univalue_path(root))
