class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ordered_strs = sorted(strs, key=len)
        prefix = ordered_strs[0]
        ordered_strs = ordered_strs[1:]
        for i in range(len(ordered_strs)):
            while (prefix not in ordered_strs[i]) and (len(prefix) >= 1):
                prefix = prefix[:-1]
            if prefix == "":
                return prefix
        return prefix
