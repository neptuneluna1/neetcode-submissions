class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = self.removeNon(s)
        s1, s2 = self.getHalves(new)
        for i in range(len(s1)):
            if s1[i] != s2[-(i+1)]:
                return False
        return True

    def getHalves(self, s: str) -> (str, str):
        length = len(s)
        half = length//2
        s1 = s[:half]
        if length % 2 == 0:
            s2 = s[half:]
        else:
            s2 = s[half+1:]
        return (s1.lower(), s2.lower())

    def removeNon(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            if s[i].isalnum():
                result += s[i]
        return result


