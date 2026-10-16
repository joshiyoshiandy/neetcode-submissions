class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpenMap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        if (len(s) <= 1):
            return False

        for c in s:
            if c in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        
        return True 