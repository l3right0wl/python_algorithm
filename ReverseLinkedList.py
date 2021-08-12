# 08 - 15
# 연결 리스트를 뒤집어라
import LinkedList

# 반복 구조로 뒤집기
class Solution1:
    def reverse_list(self, nodes: LinkedList.ListNode) -> LinkedList.ListNode:
        nextn, prevn = None, None
        nh = nodes.head

        while nh:

            nextn, nh.next = nh.next, prevn
            nh, prevn = nextn, nh

        return prevn

# 재귀 구조로 뒤집기
class Solution2:
    def reverse_list(self, head: LinkedList.Node) -> LinkedList.Node:
        def reverse(node: LinkedList.Node, prev: LinkedList.Node = None):
            if not node:
                return prev
            nextn, node.next = node.next, prev
            return reverse(nextn, node)

        return reverse(head)
