# 07 - 12
# 한 번의 거래로 낼 수 있는 최대 이익을 산출하라
import sys

# 브루트 포스로 계산
class Solution1:
    def max_profit(self, prices: list[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - price ,max_price)

        return max_price


prices = [7, 1, 5, 3, 6, 4]
sol1 = Solution1()
print(sol1.max_profit(prices))


# 저점과 현재 값과의 차이 계산
class Solution2:
    def max_profit(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)

        return profit


prices = [7, 1, 5, 3, 6, 4]
sol2 = Solution2()
print(sol2.max_profit(prices))
