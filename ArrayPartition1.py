# 07- 10
# n개의 페어를 이용한, min(a, b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

# 오름차순 풀이
class Solution1:
    def array_pair_sum(self, nums: list[int]) -> int:
        sum = 0
        pair = []
        nums.sort()

        for i in nums:
            # 앞에서부터 오름차순으로 페어를 만들어서 합 계산
            pair.append(i)
            if len(pair) % 2 == 0:
                sum += min(pair)
                pair = []

        return sum

nums = [1, 4, 3, 2]
sol1 = Solution1()
print(sol1.array_pair_sum(nums))


# 짝수 번째 값 계산
class Solution2:
    def array_pair_sum(self, nums: list[int]) -> int:
        sum = 0
        nums.sort()

        for i, n in enumerate(nums):
            # 짝수 번째 값의 합 계산
            if i % 2 == 0:
                sum += n

        return sum

nums = [1, 4, 3, 2]
sol2 = Solution2()
print(sol2.array_pair_sum(nums))


# 파이썬 다운 방식
class Solution3:
    def array_pair_sum(self, nums: list[int]) -> int:
        return sum(sorted(nums)[::2])

nums = [1, 4, 3, 2]
sol3 = Solution3()
print(sol3.array_pair_sum(nums))
