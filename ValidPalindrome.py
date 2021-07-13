# 06 - 01
# 유효한 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라.
# 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다
import collections
import re
from typing import Deque


# 리스트로 변환
class Solution1:
    def is_palindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.pop(0) != strs.pop():
                return False

        return True

sol1 = Solution1()
s = 'A man, a plan, a canal : Panama'
print(sol1.is_palindrome(s))


# 데크 자료형을 이용한 최적화
class Solution2:
    def is_palindrome(self, s: str) -> bool:
        strs: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

        return True

sol2 = Solution2()
s = 'A man, a plan, a canal : Panama'
print(sol2.is_palindrome(s))


# 슬라이싱 사용
class Solution3:
    def is_palindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)

        return s == s[::-1]

sol3 = Solution3()
s = 'A man, a plan, a canal : Panama'
print(sol3.is_palindrome(s))