# 08 - 13
# 연결 리스트가 팰린드롬 구조인지 판별하라
import collections
from typing import Deque

import LinkedList

# 리스트 변환
class Solution1:
    def is_palindrome(self, nodes: LinkedList.ListNode) -> bool:
        q: list = []

        if not nodes:
            return True

        node = nodes.head
        # Convert to list
        while node is not None:
            q.append(node.data)
            node = node.next

        # Determine palindrome
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


# 데크를 이용한 최적화
class Solution2:
    def is_palindrome(self, nodes: LinkedList.ListNode) -> bool:
        # Declare deque
        q: Deque = collections.deque()

        if not nodes:
            return True

        node = nodes.head
        # Convert to list
        while node is not None:
            q.append(node.data)
            node = node.next

        # Determine palindrome
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True


# 런너를 이용한 우아한 풀이
class Solution3:
    def is_palindrome(self, nodes: LinkedList.ListNode) -> bool:
        rev = None
        node = nodes.head
        fast = slow = node

        # Construct reverse list using runner
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next

        # Determine palindrome
        while rev and rev.data == slow.data:
            rev, slow = rev.next, slow.next

        return not rev


## 고(Go)를 이용한 데크 구현
## 고(Go)
## 데크(deque) 자료형을 고(Go)로 바닥부터 구현한 풀이
# const minCapacity = 16
#
# type Deque struct {
#     buf     []interface{}
#     head    int
#     tail    int
#     count   int
#     minCap  int
# }
#
# func (q *Deque) Len() int {
#     return q.count
# }
#
# func (q *Deque) PushBak(elem interface{}) {
#     q.growIfFull()
#
#     q.buf[q.tail] = elem
#     q.tail = q.next(q.tail)
#     q.count++
# }
#
# func (q *Deque) PopFront() interface{} {
#     if q.count <= 0 {
#         panic("deque: PopFront() called on empty queue")
#     }
#     ret := q.buf[q.head]
#     q.buf[q.head] = nil
#     q.head = q.next(q.head)
#     q.count--
#
#     return ret
# }
#
# func (q *Deque) PopBack() interface{} {
#     if q.count <= 0: {}
#         panic("deque: PopBack() called in empty queue")
#     }
#
#     q.tail. = q.prev(q.tail)
#
#     ret := q.buf[q.tail]
#     q.buf[q.tail] = nil
#     q.count--
#
#     return ret
# }
#
# func (q *Deque) prev(i int) int {
#     return (i - 1) & (len(q.buf) - 1)
# }
#
# func (q *Deque) next(i int) int {
#     return (i + 1) & (len(q.buf) - 1)
# }
#
# func (q *Deque) grwoIfFull() {
#     if len(q.buf) == 0 {
#         if q.minCap == 0{
#             q.minCap == minCapacity
#         }
#         q.buf = make([]interface{}, q.minCap)
#         return
#     }
#     if q.count == len(q.buf) {
#         q.resize()
#     }
# }
#
# func (q *Deque) resze(){
#     newBuf := make([]interface{}, q.count<<1)
#     if q.tail > q.head {
#         copy(newBuf, q.buf[q.head:q.tail])
#     } else {
#         n := copy(newBuf, q.buf[q.head:])
#         copy(newBuf[n:], q.buf[:q.tail])
#     }
#
#     q.head = 0
#     q.tail = q.count
#     q.buf = newBuf
# }
#
# func isPalindrome(head *ListNode) bool {
#     var q Deque
#
#     if head == nil {
#         return true
#     }
#     node := head
#     for node != nil {
#         q.PushBack(node.Val)
#         node = node.next
#     }
#
#     for q.Len() > 1 {
#         if q.PopFront() != q.PopBack() {
#             return false
#         }
#     }
#
#     return true
# }
