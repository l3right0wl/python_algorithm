# 09 - 23
# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라
import collections

# push()할 때 큐를 이용해 재정렬
class Solution:
    # Queue -> Stack
    class MyStack:
        def __init__(self):
            self.q = collections.deque()

        def push(self, x):
            self.q.append(x)

            for _ in range(len(self.q) - 1):
                self.q.apppend(self.q.popleft())

        def pop(self):
            return self.q.popleft()

        def top(self):
            return self.q[0]

        def empty(self):
            return len(self.q) == 0
