class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

        
class ListNode:
    def __init__(self):
        self.head = None
        self.count = 0

    # 추가 (마지막 값)
    def add(self, node):
        if self.head is None:
            self.head = node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
        self.count += 1
