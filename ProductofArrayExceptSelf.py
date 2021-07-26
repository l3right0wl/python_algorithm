# 07 - 11
# 배열을 입력받아 out[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라.

# 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
class Solution1:
    def product_except_self(self, nums: list[int]) -> list[int]:
        out = []
        p = 1
        # 왼쪽 곱셈
        for i in range(len(nums)):
            out.append(p)
            p = p * nums[i]

        p = 1
        # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
        for j in range(len(nums)-1, 0-1, -1):
            out[j] = out[j] * p
            p = p * nums[j]

        return out

nums = [1, 2, 3, 4]
sol1 = Solution1()
print(sol1.product_except_self(nums))