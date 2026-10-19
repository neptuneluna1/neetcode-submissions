class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        lens = {1: len(word1), 2: len(word2)}
        length = min(lens.values())
        word = min(lens, key=lens.get)
        result = ""
        for i in range(length):
            result += word1[i]
            result += word2[i]
        if word == 1:
            result += word2[length:]
        else:
            result += word1[length:]
        return result
        