"""
정렬된 배열을 이진 탐색 트리로 변환 (Convert Sorted Array to Binary Search Tree)

오름차순으로 정렬된 정수 배열 nums가 주어질 때, 높이 균형 이진 탐색 트리로 변환하라.

입력: nums = [-10, -3, 0, 5, 9]
출력: [0, -3, 9, -10, null, 5]
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(nums: list[int]) -> TreeNode | None:
    def dfs(start, end):
        if start > end:
            return None

        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = dfs(start, mid - 1)
        node.right = dfs(mid + 1, end)
        return node

    return dfs(0, len(nums) - 1)


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    result = sorted_array_to_bst(nums)
