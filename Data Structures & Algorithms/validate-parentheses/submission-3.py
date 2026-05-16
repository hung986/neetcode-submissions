class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for b in s:
            if b not in mapping:
                stack.append(b)
            else:
                if not stack:
                    return False
                if stack[-1] != mapping[b]:
                    return False
                stack.pop()
        return not stack