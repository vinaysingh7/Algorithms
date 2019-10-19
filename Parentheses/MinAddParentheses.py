class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        i, left, right = 0, 0, 0
        while i < len(s):
            if s[i] == '(':
                left += 1
            else:
                right += 1
            if right > left:
                ans += 1
                left += 1
            i += 1       
        if left > right:
            ans += left-right
        return ans

s = "()))(("
sol =Solution()
print(sol.minAddToMakeValid(s))

23280665011553