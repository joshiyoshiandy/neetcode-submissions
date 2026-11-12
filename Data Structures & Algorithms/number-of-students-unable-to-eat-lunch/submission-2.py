class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        cnt = {0 : 0, 1 : 0}
        
        for st in students:
            cnt[st] += 1

        for sn in sandwiches:
            if cnt[sn] > 0:
                cnt[sn] -= 1
            else:
                break

        return cnt[0] + cnt[1]