# 07 -08
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

# 투 포인터를 최대로 이동
class Solution1():
     def trap(self, height: list[int]) -> int:
         if not height:
             return 0

         volume = 0
         left, right = 0, len(height) - 1
         max_left, max_right = height[left], height[right]

         while left < right:
            max_left, max_right = max(height[left], max_left), \
                                  max(height[right], max_right)
            # 더 높은 쪽을 향해 투 포인터 이동
            if max_left <= max_right:
                volume += max_left - height[left]
                left += 1
            else:
                volume += max_right - height[right]
                right -= 1

         return volume

sol1 = Solution1()
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol1.trap(heights))

# 스택 쌓기
class Solution2:
    def trap(self, height: list[int]) -> int:
        stack = []
        volume = 0

        for i in range(len(height)):
            # 변곡점을 만나는 경우
            while stack and height[i] > height[stack[-1]]:
                 # 스택에서 꺼낸다
                top = stack.pop()

                if not len(stack):
                    break

                # 이전과의 차이만큼 물 높이 처리
                distance = i - stack[-1] - 1
                waters = min(height[i], height[stack[-1]]) - height[top]

                volume += distance * waters

            stack.append(i)
        return volume

sol2 = Solution2()
heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(sol2.trap(heights))