class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for i in range(len(operations)):
            length = len(record)
            if operations[i] == '+':
                record.append(record[length-1] + record[length-2])
            elif operations[i] == 'D':
                record.append(record[length-1] * 2)
            elif operations[i] == 'C':
                record = record[0:length-1]
            else:
                record.append(int(operations[i]))
        print(record)
        return sum(record)