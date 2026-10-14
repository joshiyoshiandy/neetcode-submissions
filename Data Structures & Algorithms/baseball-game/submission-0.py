class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        res = 0

        for op in operations:
            if op == "+" and len(record) >= 2:
                n2 = record.pop()
                n1 = record.pop()
                sm = n1 + n2
                record.append(n1)
                record.append(n2)
                record.append(sm)
            elif op == "D" and len(record) > 0:
                n1 = record.pop()
                sm = 2 * n1
                record.append(n1)
                record.append(sm)
            elif op == "C" and len(record) > 0:
                record.pop()
            else:
                record.append(int(op))
        
        for r in record:
            res += r

        return res
