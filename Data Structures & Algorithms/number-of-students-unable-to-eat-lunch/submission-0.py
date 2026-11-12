class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        curSandwich = 0
        curStudent = 0
        studentCount = len(students)
        numRequeue = 0

        while curSandwich < len(sandwiches) and numRequeue < studentCount:
            if students[curStudent] == sandwiches[curSandwich]:
                curSandwich += 1
                numRequeue = 0
            else:
                students.append(students[curStudent])
                numRequeue += 1
            
            curStudent += 1

        return len(students) - curStudent