class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) < 2):
            return False

        closeToOpenMap = {")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for c in s:
            if c in closeToOpenMap.keys():
                if stack and stack[-1] == closeToOpenMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0