# 09 - 24
# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라

# 스택 2개 사용
class Solution:
    # Stack -> Queue
    class MyQueue:
        def __init__(self):
            self.input = []
            self.output = []

        def push(self, x):
            self.input.append(x)

        def pop(self):
            self.peek()
            return self.output.pop()

        def peek(self):
            if not self.output:
                while self.input:
                    self.output.append(self.input.pop())
            return self.output[-1]

        def empty(self):
            return len(self.input) == 0 and len(self.output) == 0
