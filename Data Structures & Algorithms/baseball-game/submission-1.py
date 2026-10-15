class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        res = 0

        for op in operations:
            if op == "+" and len(record) >= 2:
                n = record[-1] + record[-2]
                res += n
                record.append(n)
            elif op == "D" and len(record) > 0:
                n = 2 * record[-1]
                res += n
                record.append(n)
            elif op == "C" and len(record) > 0:
                res -= record[-1]
                record.pop()
            else:
                res += int(op)
                record.append(int(op))
                
        return res
