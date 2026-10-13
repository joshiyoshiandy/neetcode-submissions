class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        res = [0] * n

        for i in range(n):
            highest_right = -1
            for j in range(i + 1, n):
                highest_right = max(highest_right, arr[j])
            res[i] = highest_right

        return res
