def count_palindromic_subsequences(s):
    print("here")
    if len(s) == 1: return 1
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            # if j == i+1:
            #     dp[i][j] = 2 if s[i] == s[j] else 1
            if s[i] == s[j]:
                dp[i][j] = dp[i][j-1] + dp[i+1][j] +1 - dp[i+1][j-1]
            else:
                dp[i][j] = dp[i][j-1] + dp[i+1][j] - dp[i+1][j-1]
    print("jojo", dp)
    return dp[0][n-1]

print(count_palindromic_subsequences("aaaa"))