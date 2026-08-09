class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr[0] = max(arr)
        for i in range(len(arr)):
            if i == len(arr)-1:
                arr[i] = -1
            else:
                arr[i] = max(arr[i+1:])
        return arr
