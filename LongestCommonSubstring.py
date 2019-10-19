# Given two strings X and Y. The task is to find the length of the longest common substring.

# Example:
# Testcase 1: CDGH is the longest substring present in both of the strings.
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        if not A or not B:
            return 0
        m = len(A)
        n = len(B)
        arr = [[0 for i in range(n+1)] for i in range(m+1)]
        result = (0,0)
        max_len = 0
        for i in range(0, m):
            for j in range(0, n):
                if A[i] == B[j]:
                    arr[i+1][j+1] = arr[i][j] + 1
                    if max_len < arr[i+1][j+1]:
                        max_len = arr[i+1][j+1]
                        result = (i+1, j+1)
        i = result[0]
        result = []
        while i > 0 and j > 0 and arr[i][j] != 0:
            result.append(A[i-1])
            i -= 1
            j -= 1
        print(''.join(result[::-1]))
        return ''.join(result[::-1])

sol = Solution()
sol.longestCommonSubstring('ABCDGH', 'ACDGHR')