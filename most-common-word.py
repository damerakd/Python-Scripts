import collections
from collections import Counter

class MostCommonWord:
    def find_most_common_word(self, paragraph, banned_word):
        for char in "!?',;.":
            paragraph = paragraph.replace(char, " ")
        count = collections.Counter(
            word for word in paragraph.lower().split())
        count = count.most_common()
        print(count)
        banned_word = set(banned_word)
        for word in count:
            if word[0] not in banned_word:
                return word

mostcommonword = MostCommonWord()
mostcommonword.find_most_common_word("Bob. hIt, baLl",["bob", "hit"])