# 06 - 02
# 문자열 뒤집기
# 문자열을 뒤집는 함수를 작성하라.
# 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.

# 투 포인터를 이용한 스왑
class Solution1:
    def reverse_string(self, s: list[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

sol1 = Solution1()
s1 = ['h', 'e', 'l', 'l', 'o']
sol1.reverse_string(s1)
print(s1)


# 파이썬 다운 방식
# reverse 함수
class Solution2:
    def reverse_string(self, s: list[str]) -> None:
        s.reverse()

sol2 = Solution2()
s2 = ['H', 'a', 'n', 'n', 'a', 'h']
sol2.reverse_string(s2)
print(s2)


# 문자열 슬라이싱
s3 = ['H', 'e', 'l', 'l', 'o', 'W', 'o', 'r', 'l', 'd']
# 공간 복잡도 O(1)로 제한할 경우 변수 할당에 제약이 있어 동작 안할 수 있음
s3 = s3[::-1]
print(s3)
# 다음과 같은 트릭을 사용하면 동작함
s3[:] = s3[::-1]
print(s3)
