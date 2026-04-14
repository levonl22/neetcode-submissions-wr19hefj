class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")" : "(", "}" : "{", "]" : "["}
        stack = []
        if not s:
            return False

        for c in s:
            if not stack and c in brackets:
                return False
            if c in brackets and stack[-1] == brackets[c]:
                stack.pop()
            else:
                stack.append(c)
        
        return not stack