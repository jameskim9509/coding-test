"""
두 연결리스트의의 덧셈을 역순으로
ex) (2 -> 4 -> 3) + (5 -> 6 -> 4) = (7 -> 0 -> 8)

point1. 전가산기 알고리즘
point2. root의 next 노드부터 값을 채워 마지막 빈 노드가 생기지 않도록 구현
point3. carry는 다음 루프에 반영
"""


class ListNode:
    """
    연결리스트를 위한 노드
    """

    def __init__(self, value: int):
        self.next: ListNode = None
        self.val = value


def reverse_add_two_linked_list(n1: ListNode, n2: ListNode) -> ListNode:
    """
    두 연결 리스트를 역순으로 합함
    """

    head = root = ListNode(0)
    carry = 0
    while n1 or n2 or carry != 0:
        total = 0
        if n1:
            total += n1.val
            n1 = n1.next
        if n2:
            total += n2.val
            n2 = n2.next

        carry, val = (total + carry) // 10, (total + carry) % 10
        head.next = ListNode(val)
        head = head.next

    return root.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    result = reverse_add_two_linked_list(l1, l2)
    result_str: str = ""
    while result:
        if result.next:
            result_str += f"{result.val} -> "
        else:
            result_str += f"{result.val}"
        result = result.next
    print(result_str)
