"""
홀짝 연결 리스트
입력: 2->1->3->5->6->4->7->NULL
출력: 2->3->6->7->1->5->4->NULL
"""


class ListNode:
    """
    연결리스트 노드
    """

    def __init__(self, value):
        self.value: int = value
        self.next: ListNode = None


def change_to_odd_even_list(head: ListNode):
    """
    연결리스트를 홀짝 연결리스트로 변경
    """
    if head is None:
        return None

    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head
    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head
    return odd_head


if __name__ == "__main__":
    node = ListNode(2)
    node.next = ListNode(1)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(5)
    node.next.next.next.next = ListNode(6)
    node.next.next.next.next.next = ListNode(4)
    node.next.next.next.next.next.next = ListNode(7)
    result_node = change_to_odd_even_list(node)

    RESULT_STR: str = ""
    while result_node:
        if result_node is not None:
            RESULT_STR = RESULT_STR + f"{result_node.value}->"
        result_node = result_node.next
    print(RESULT_STR + "->NULL")
