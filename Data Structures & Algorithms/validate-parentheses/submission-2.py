class Solution:
    def isValid(self, s: str) -> bool:
        openingbracket = ['(', '[', '{']
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for b in s:
            if b in openingbracket:
                stack.append(b)
            else:
                if not stack:
                    return False
                if stack.pop() != mapping[b]:
                    return False
        return not stack