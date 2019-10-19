"""
Base Case: arr[i][i] = True for each char and if s[i] == s[i+1] arr[i][i+1] = True
i -> n to 0, j -> 0 to n
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = len(s)
        dp = [[False for i in range(m)] for i in range(m)]
        length, index = 1, 0
        for i in range(m-1, -1, -1):
            dp[i][i] = True
            if i < m-1 and s[i] == s[i+1]:
                dp[i][i+1] = True
                if length < 2:
                    length, index = 2, i
            for j in range(i+1, m):
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if j-i+1 >= length:
                        length, index = j-i+1, i

        return s[index: index+length]
                    