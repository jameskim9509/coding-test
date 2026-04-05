"""
두 이진 트리 병합 (Merge Two Binary Trees)

두 이진 트리의 루트가 주어질 때, 두 트리를 병합하라.
두 노드가 겹치면 값을 합산하고, 겹치지 않으면 존재하는 노드를 그대로 사용한다.

입력: root1 = [1, 3, 2, 5], root2 = [2, 1, 3, null, 4, null, 7]
출력: [3, 4, 5, 5, 4, null, 7]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def merge_trees(root1: TreeNode | None, root2: TreeNode | None) -> TreeNode | None:
    def dfs(node1: TreeNode | None, node2: TreeNode | None):
        if node1 and node2:
            node1.val = node1.val + node2.val
            node1.left = dfs(node1.left, node2.left)
            node1.right = dfs(node1.right, node2.right)
            return node1
        else:
            return node1 or node2

    dfs(root1, root2)
    return root1


if __name__ == "__main__":
    root1 = TreeNode(1, TreeNode(3, TreeNode(5)), TreeNode(2))
    root2 = TreeNode(2, TreeNode(1, None, TreeNode(4)), TreeNode(3, None, TreeNode(7)))
    result = merge_trees(root1, root2)
