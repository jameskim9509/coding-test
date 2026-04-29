"""
연결 리스트 삽입 정렬 (Insertion Sort List)

연결 리스트의 head가 주어졌을 때, 삽입 정렬을 이용해 오름차순으로 정렬된 리스트를 반환하라.

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


def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = head

    while cur:
        nxt = cur.next
        prev = dummy
        temp = dummy.next
        while temp and temp.val < cur.val:
            prev = temp
            temp = temp.next
        prev.next = cur
        cur.next = temp
        cur = nxt

    return dummy.next


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
    print(to_list(insertion_sort_list(to_linked_list([4, 2, 1, 3]))))
    print(to_list(insertion_sort_list(to_linked_list([-1, 5, 3, 4, 0]))))
    print(to_list(insertion_sort_list(to_linked_list([]))))
