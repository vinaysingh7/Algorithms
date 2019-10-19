class Solution:
    def mergeSort(self, arr):
        n = len(arr)
        if n < 2:
            return arr
        m = len(arr)//2

        left = self.mergeSort(arr[:m])
        right = self.mergeSort(arr[m:])
        return self.merge(left, right)
    
    def merge(self, arr1, arr2):
        if not arr1 or not arr2:
            return arr1 if arr1 else arr1
        i, j = 0, 0
        m, n = len(arr1), len(arr2)
        arr = []
        while i < m and j < n:
            if arr1[i] < arr2[j]:
                arr += arr1[i],
                i += 1
            else:
                arr += arr2[j],
                j += 1
        if i < m:
            arr.extend(arr1[i:])
        if j < n:
            arr.extend(arr2[j:])
        return arr

sol = Solution()
result = sol.mergeSort([5,1,1,2,0,0])
result = sol.mergeSort([1])
print(result)


    #     if len(arr) <= 1:
    #         return arr
        
    #     m = len(arr)//2

    #     left = self.mergeSort(arr[:m])
    #     right = self.mergeSort(arr[m:])
    #     return self.merge(left, right)
    
    # def merge(self, arr1, arr2):
    #     if not arr1 or not arr2:
    #         return arr1 if not arr2 else arr1
        
    #     i, j = 0, 0
    #     arr = []
        
    #     while i < len(arr1) and j < len(arr2):
    #         if arr1[i] < arr2[j]:
    #             arr.append(arr1[i])
    #             i += 1
    #         else:
    #             arr.append(arr2[j])
    #             j += 1                
        
    #     if i < len(arr1):
    #         arr.extend(arr1[i:])
    #     elif j < len(arr2):
    #         arr.extend(arr2[j:])

    #     return arr