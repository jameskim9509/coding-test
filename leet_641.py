"""
원형데크 디자인

MyCircularDequeue(k): 데크 사이즈를 k로 지정하는 생성자
insertFront(): 데크 처음에 아이템을 추가하고 성공할 경우 true 반환
insertLast(): 데크 마지막에 아이템을 추가하고 성공할 경우 true 반환
deleteFront(): 데크 처음에 아이템을 삭제하고 성공할 경우 true 반환
deleteLast(): 데크 마지막에 아이템을 삭제하고 성공할 경우 true 반환
getFront(): 데크의 첫번째 아이템 get, 비어있을 경우 -1 반환
getRear(): 데크의 마지막 아이템 get, 비어있을 경우 -1 반환
isEmpty(): 데크가 비어있는지 여부 판별
isFull(): 데크가 가득 차 있는지 여부 판별
"""


class ListNode:
    def __init__(self, value):
        self.value = value
        self.left: ListNode = None
        self.right: ListNode = None


class MyCircluarDequeue:
    def __init__(self, k: int):
        self.front, self.rear = ListNode(None), ListNode(None)
        self.front.right = self.front.left = self.rear
        self.rear.left = self.rear.right = self.front
        self.length = 0
        self.size = k

    def insertFront(self, value) -> bool:
        if self.length >= self.size:
            return False
        prev = self.front
        self.front = ListNode(value)
        self.front.right, prev.left = prev, self.front
        self.front.left, self.rear.right = self.rear, self.front
        self.length += 1
        return True

    def insertLast(self, value) -> bool:
        if self.length >= self.size:
            return False
        prev = self.rear
        self.rear = ListNode(value)
        self.rear.left, prev.right = prev, self.rear
        self.rear.right, self.front.left = self.front, self.rear
        self.length += 1
        return True

    def deleteFront(self) -> bool:
        if not self.front.value:
            return False

        if self.length <= 0:
            return False

        prev = self.front
        prev.right = None
        self.front = self.front.right
        self.front.left, self.rear.right = self.rear, self.front
        self.length -= 1
        return True

    def deleteRear(self) -> bool:
        if not self.rear.value:
            return False

        if self.length <= 0:
            return False

        prev = self.rear
        prev.left = None
        self.rear = self.rear.left
        self.front.left, self.rear.right = self.rear, self.front
        self.length -= 1
        return True

    def getFront(self):
        if self.front.value:
            return self.front.value
        return -1

    def getLast(self):
        if self.rear.value:
            return self.rear.value
        return -1

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isFull(self):
        if self.size <= self.length:
            return True
        return False
