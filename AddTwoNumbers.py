# 08 - 16
# 역순으로 저장된 연결 리스트의 숫자를 더하라
import LinkedList

# 자료형 변환
class Solution1:
    # 연결리스트 뒤집기
    def reverse_list(self, ll: LinkedList.ListNode) -> LinkedList.ListNode:
        lh = ll.head
        node, prevn = lh, None

        while node:
            nextn, node.next = node.next, prevn
            prevn, node = node, nextn

        return prevn

    # 연결리스트를 파이썬 리스트로 변환
    def to_list(self, node: LinkedList.ListNode) -> LinkedList.Node:
        l_list: list = []
        while node:
            l_list.append(node.data)
            node = node.next
        return l_list

    # 파이썬 리스트를 연결 리스트로 변환
    def to_reversed_linkedlist(self, result: LinkedList.Node) -> LinkedList.Node:
        prevn: LinkedList.Node = None
        for r in result:
            node = LinkedList.Node(r)
            node.next = prevn
            prevn = node

        return node

    def add_two_numbers(self, l1: LinkedList.ListNode, l2: LinkedList.ListNode) -> LinkedList.ListNode:
        a = self.to_list(self.reverse_list(l1))
        b = self.to_list(self.reverse_list(l2))

        result_str = int(''.join(str(e) for e in a)) + int(''.join(str(e) for e in b))

        # 최종 계산 결과 연결 리스트 변환
        return self.to_reversed_linkedlist(str(result_str))




# 전가산기 구현
class Solution2:
    def add_two_numbers(self, l1: LinkedList.Node, l2: LinkedList.Node) -> LinkedList.Node:
        root = head = LinkedList.Node(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            # 두 입력값의 합 계산
            if l1:
                sum += l1.data
                l1 = l1.next
            if l2:
                sum += l2.data
                l2 = l2.next

            # 몫(자리올림수)과 나머지(값) 계산
            carry, data = divmod(sum+carry, 10)
            head.next = LinkedList.Node(data)
            head = head.next

        return root.next

