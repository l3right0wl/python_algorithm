# 09 -26
# 다음 연산을 제공하는 원형 데크를 디자인하라
# MyCircularDeque(k): 데크 사이즈를 k로 지정하는 생성자다.
# insertFront(): 데크 처음에 아이템을 추가하고 성공할 경우 true를 리턴한다.
# insertLast(): 데크 마지막에 아이템을 추가하고 성공할 경우 true를 리턴한다.
# deleteFront(): 데크 처음에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
# deleteLast(): 데크 마지막에 아이템을 삭제하고 성공할 경우 true를 리턴한다.
# getFront(): 데크의 첫 번째 아이템을 가져온다. 데크가 비어있다면 -1을 리턴한다.
# getRear(): 데크의 마지막 아이템을 가져온다. 데크가 비어 있다면 -1을 리턴한다.
# isEmpty(): 데크가 비어 있는지 여부를 판별하라.
# isFull(): 데크가 가득 차 있는지 여부를 판별하라.

class ListNode:
    def __init__(self, val):
        self.data = val
        self.next = None

# 이중 연결 리스트를 이용한 데크 구현
class MyCircularDeque:
    def __init__(self, k):
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.length = k, 0
        self.head.right, self.tail.left = self.tail, self.head

    def _add(self, node: ListNode, new: ListNode):
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insert_front(self, value: int) -> bool:
        if self.length == 0:
            return False
        self.length += 1
        self._add(self.head, ListNode(value))
        return True

    def insert_last(self, value: int) -> bool:
        if self.length == 0:
            return False
        self.length += 1
        self._add(self.tail.left, ListNode(value))
        return True

    def delete_front(self) -> bool:
        if self.length == 0:
            return False
        self.length -= 1
        self._del(self.head)
        return True

    def delete_last(self) -> bool:
        if self.length == 0:
            return False
        self.length -= 1
        self._del(self.tail.left.left)
        return True

    def get_front(self):
        if self.length:
            return self.head.right.data
        else:
            return -1

        # Python Code
        # return self.head.right.data if self.length else -1

    def get_rear(self):
        if self.length:
            return self.tail.left.data
        else:
            return -1

        # Python Code
        # return self.tail.left.data if self.length else -1

    def is_empty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False

        # Python Code
        # return self.length == 0

    def is_full(self) -> bool:
        if self.length == self.k:
            return True
        else:
            return False

        # Python Code
        # return self.length == self.k
