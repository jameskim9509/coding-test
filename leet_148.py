"""
연결 리스트 정렬 (Sort List)

연결 리스트의 head가 주어졌을 때, 오름차순으로 정렬된 리스트를 반환하라.

입력: head = [4, 2, 1, 3]
출력: [1, 2, 3, 4]

입력: head = [-1, 5, 3, 4, 0]
출력: [-1, 0, 3, 4, 5]

입력: head = []
출력: []
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


def merge_list(l1: ListNode, l2: ListNode) -> ListNode:
    if l1 and l2:
        if l1.val > l2.val:
            l1, l2 = l2, l1
        l1.next = merge_list(l1.next, l2)

    return l1 or l2


def sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    l1 = sort_list(head)
    l2 = sort_list(mid)

    return merge_list(l1, l2)


def to_list(head: Optional[ListNode]) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def to_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode()
    node = dummy
    for v in values:
        node.next = ListNode(v)
        node = node.next
    return dummy.next


if __name__ == "__main__":
    print(to_list(sort_list(to_linked_list([4, 2, 1, 3]))))
    print(to_list(sort_list(to_linked_list([-1, 5, 3, 4, 0]))))
    print(to_list(sort_list(to_linked_list([]))))
