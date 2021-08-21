# 09 - 25
# 원형 큐를 디자인하라

# 배열을 이용한 풀이
class Solution:
    # Circular Queue
    class MyCircularQueue:
        def __init__(self, k: int):
            self.q = [None] * k
            self.maxlen = k
            # p1 = front
            self.p1 = 0
            # p2 = rear
            self.p2 = 0

        # enQueue(): rear 포인터 이동
        def en_queue(self, data: int) -> bool:
            if self.q[self.q2] is None:
                self.q[self.q2] = data
                self.p2 = (self.p2 + 1) % self.maxlen
                return True
            else:
                return False

        # deQueue(): front 포인터 이동
        def de_queue(self) -> bool:
            if self.q[self.p1] is None:
                return False
            else:
                self.q[self.p1] = None
                self.p1 = (self.p1 + 1) % self.maxlen
                return True

        def front(self) -> int:
            if self.q[self.p1] is None:
                return None
            else:
                return self.q[self.p1]

            # Python Code
            # return -1 if self.q[self.p1] is None else self.q[self.p1]

        def rear(self) -> int:
            if self.q[self.p2] is None:
                return None
            else:
                return self.q[self.p2]

            # Python Code
            # return -1 if self.q[self.p2] is None else self.q[self.p2]

        def is_full(self) -> bool:
            if self.p1 == self.p2 and self.q[self.p1] is not None:
                return True
            else:
                return False

            # Python Code
            # return self.p1 == self.p2 and self.q[self.p1] is not None

        def is_empty(self) -> bool:
            if self.p1 == self.p2 and self.q[self.p1] is None:
                return True
            else:
                return False

            # Python Code
            # return self.p1 == self.p2 and self.q[self.p1] is None
