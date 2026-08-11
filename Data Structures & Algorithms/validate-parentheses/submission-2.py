class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False
        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                if len(stack) == 0: return False
                var = stack[-1]
                if (var == '(' and char != ')') or (var == '{' and char != '}') or (var == '[' and char != ']'):
                    return False
                else:
                    stack.pop()
        if len(stack) == 0: return True
        return False
        