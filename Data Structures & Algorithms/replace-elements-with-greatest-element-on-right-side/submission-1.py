class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n
        highest = -1

        for i in range(n - 1, -1, -1):
            res[i] = highest
            highest = max(highest, arr[i])

        return res
