# 06 - 04
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.
import collections
import re

# 리스트 컴프리헨션, Counter 객체 사용
class Solution1():
    def most_common_word(self, paragraph: str, banned: list[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ',paragraph)
            .lower().split()
                    if word not in banned]

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]

sol1 = Solution1()
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
print(sol1.most_common_word(paragraph, banned))

