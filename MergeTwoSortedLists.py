# 08 - 13
# 정렬되어 있는 두 연결 리스트를 합쳐라

import LinkedList

class Solution1:
    def mergeTwoLists(self, l1: LinkedList.Node, l2: LinkedList.Node) -> LinkedList.Node:

        if (not l1) or (l2 and l1.data > l2.data):
            l1, l2 = l2, l1

        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

