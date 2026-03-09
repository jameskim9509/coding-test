"""
유효한 괄호
입력: ()[]{}
출력: true
"""


class Node:
    """
    연결리스트 노드
    """

    def __init__(self, value, next):
        self.value = value
        self.next = next


class Stack:
    """
    연결리스트로 구성된 스택
    """

    def __init__(self):
        self.last = None

    def push(self, value):
        """
        선입
        """
        self.last = Node(value, self.last)

    def pop(self):
        """
        선출
        """
        last_node = self.last
        if last_node is None:
            return None

        self.last = last_node.next
        return last_node.value

    def is_empty(self):
        """
        스택 empty 여부 확인
        """
        return self.last is None


def is_valid_parentheses(in_str: str):
    """
    괄호 유효성 확인
    """

    st = Stack()
    for ch in in_str:
        if ch == ")" and st.pop() != "(":
            return False
        if ch == "]" and st.pop() != "[":
            return False
        if ch == "}" and st.pop() != "{":
            return False
        elif ch == "(" or ch == "[" or ch == "{":
            st.push(ch)

    if st.is_empty():
        return True

    return False


if __name__ == "__main__":
    INPUT_STR = "()[]{}"
    print(is_valid_parentheses(INPUT_STR))
