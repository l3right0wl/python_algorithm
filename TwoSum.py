# 07 - 07
# 덧셈하여 타켓을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

# 브루트 포스로 계산
class Solution1:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


sol1 = Solution1()
nums1 = [2, 7, 11, 15]
target1 = 9
print(sol1.two_sum(nums1, target1))


# in을 이용한 탐색
class Solution2:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        for i, n in enumerate(nums):
            complement = target - n

            if complement in nums[i+1:]:
                return nums.index(n), nums[i+1:].index(complement) + (i+1)


sol2 = Solution2()
nums2 = [2, 7, 11, 15]
target2 = 9
print(sol2.two_sum(nums2, target2))


# 첫 번째 수를 뺀 결과 키 조회
class Solution3:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 키와 값을 바꿔서 딕셔너리로 저장
        for i, num in enumerate(nums):
            nums_map[num] = i

        # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return nums.index(num), nums_map[target - num]


sol3 = Solution3()
nums3 = [2, 7, 11, 15]
target3 = 9
print(sol3.two_sum(nums3, target3))


# 조회 구조 개선
class Solution4:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        nums_map = {}
        # 하나의 for문으로 통합
        for i, num in enumerate(nums):
            print(i, num)
            if target - num in nums_map:
                print(target - num, nums_map)
                return [nums_map[target - num], i]
            nums_map[num] = i
            print(nums_map)

sol4 = Solution4()
nums4 = [2, 7, 11, 15]
target4 = 9
print(sol4.two_sum(nums4, target4))


# 투 포인터 이용
# 입력값인 nums가 정렬된 상태가 아니기 때문에 투 포인터로 풀 수 없다
# 가령 sort()를 사용하여 정렬하더라도 본래의 인덱스를 찾을 수 없기때문에
# 인덱스가 아닌 값을 찾아내는 문제라면 사용 가능
# 매우 빠른 속도 기대
class Solution5:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        # nums.sort()
        left, right  = 0, len(nums) - 1
        while not left == right:
            # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
            if nums[left] + nums[right] < target:
                left += 1
            # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                return left, right


# 고(GO)구현
# 제일 빠른 속도의 Go언어 알고리즘
# class GoSolution:
#     func twoSum(nums []int, target int) []int {
#         numsMap := make(map[int]int)
#
#         # 키와 값을 바꿔서 딕셔너리로 저장
#         for i, num := range nums {
#             numsMap[num] = i
#         }
#
#         # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
#         for i, num := range nums {
#             if j, ok := numsMap[target-num]; ok && i!= j {
#                 return []int{i, j}
#             }
#         }
#
#     return []int{}
#   }

