class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for x in range(len(operations)):
            if operations[x] == '+':
                record.append(sum(record[-2:]))
            elif operations[x] == 'D':
                record.append(record[-1] * 2)
            elif operations[x] == 'C':
                record.pop()
            else:
                record.append(int(operations[x]))
        return sum(record)
