# 06 - 05
# 문자열 배열을 받아 애너그램 단위로 그룹핑해라
import collections

# 정렬하여 딕셔너리에 추가
class Solution1():
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = collections.defaultdict(list)

        for word in strs:
            # 정렬하여 딕셔너리에 추가
            anagrams[''.join(sorted(word))].append(word)

        return anagrams.values()

sol1 = Solution1()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(sol1.group_anagrams(input))
