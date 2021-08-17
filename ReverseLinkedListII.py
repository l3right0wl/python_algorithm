# 08 - 19
# 인덱스 m에서 n까지를 역순으로 만들어라
# 인덱스 m은 1부터 시작한다
import LinkedList

# 반복 구조로 노드 뒤집기
class Solution1:
    def reverse_between(self, head: LinkedList.Node, m: int, n: int) -> LinkedList.Node:
        # 예외처리
        if not head or m == n :
            return head

        root = start = LinkedList.Node(None)
        root.next = head
        # start, end 지정
        for _ in range(m-1):
            start = start.next
        end = start.next

        # 반복하면서 노드 차례대로 뒤집기
        for _ in range(m-n):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next

