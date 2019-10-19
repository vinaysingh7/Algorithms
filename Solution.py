class Solution:
    def permute(self, nums):
        
        results = []
        def dfs(l, r, nums):
            if l == r:
                print(nums)
                results.append(nums)
                return
            
            for i in range(l, r+1):
                # print(i, l)
                nums[i], nums[l] = nums[l], nums[i]
                dfs(l+1, r, nums)
                # print(i, l)
                nums[i], nums[l] = nums[l], nums[i]
                
        dfs(0, len(nums)-1, nums)             

sol = Solution()
sol.permute([1,2,3])
