class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length-(i+1)]:
                temp = s[length-(i+1)]
                s[length-(i+1)] = s[i]
                s[i] = temp
        return s

        