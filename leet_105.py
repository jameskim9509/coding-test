"""
전위/중위 순회로부터 이진 트리 구성 (Construct Binary Tree from Preorder and Inorder Traversal)

트리의 전위(preorder) 순회 결과와 중위(inorder) 순회 결과가 주어질 때,
원래의 이진 트리를 구성하여 반환하라.

입력: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
출력: [3, 9, 20, null, null, 15, 7]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode | None:
    def dfs(in_orders: list[int]):
        if not in_orders:
            return None

        find_val = preorder.pop(0)
        root_ind = in_orders.index(find_val)
        node = TreeNode(find_val)
        node.left = dfs(in_orders[:root_ind])
        node.right = dfs(in_orders[root_ind + 1 :])

        return node

    return dfs(inorder)


if __name__ == "__main__":
    root = build_tree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    print(root)
