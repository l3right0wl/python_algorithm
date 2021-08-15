# 08 - 17
# 연결 리스트를 입력받아 페어 단위로 스왑하라
import LinkedList

# 값만 교환
class Solution1:
    def swap_pairs(self, head: LinkedList.Node) -> LinkedList.Node:
        cur = head

        while cur and cur.next:
            # 값만 교환
            cur.data, cur.next.data = cur.next.data, cur.data
            cur = cur.next.next

        return head


# 반복 구조로 스왑
class Solution2:
    def swap_pairs(self, head: LinkedList.Node) -> LinkedList.Node:
        root = prevn = LinkedList.Node(None)
        prevn.next = head
        while head and head.next:
            # b가 a(head)를 가리키도록 할당
            b = head.next
            head.next = b.next
            b.next = head

            # prevn가 b를 가리키도록 할당
            prevn.next = b

            # 다음번 비교를 위해 이동
            head = head.next
            prevn = prevn.next.next
        return root.next


# 재귀 구조로 스왑
class Solution3:
    def swap_pairs(self, head: LinkedList.Node) -> LinkedList.Node:
        if head and head.next:
            p = head.next
            # 스왑된 리턴 받음
            head.next = self.swap_pairs(p.next)
            p.next = head
            return p
        return head
