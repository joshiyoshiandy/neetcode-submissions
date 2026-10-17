class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        res = self.stack[0]
        
        for s in self.stack:
            if s < res:
                res = s

        return res
