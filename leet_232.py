"""
스택을 이용한 큐 구현
push(x), pop(), peek(), empty() 함수 구현하기

예시)
queue.push(1);
queue.push(2);
queue.peek(); // 1
queue.pop(); // 1
queue.empty(); // false
"""


class MyQueue:
    """
    custom queue
    """

    def __init__(self):
        self.left_st = []
        self.right_st = []

    def push(self, value):
        """
        queue.push
        """

        self.left_st.append(value)

    def pop(self):
        """
        queue.pop
        """

        while len(self.left_st) != 0:
            self.right_st.append(self.left_st.pop())
        return self.right_st.pop()

    def peek(self):
        """
        queue.peek
        """

        while len(self.left_st) != 0:
            self.right_st.append(self.left_st.pop())
        return self.right_st[-1]

    def empty(self):
        """
        return whether queue is empty
        """

        if len(self.left_st) == 0 or len(self.right_st) == 0:
            return False
        return True


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())
