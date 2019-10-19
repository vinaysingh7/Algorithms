s = "ab(a(c)fg)9)"
s = ")a(b)c()("
s = ")("
s = "a(b))"
s = "(a(c()b)"
s = "(a)b(c)d(e)f)(g)"
ans = []
min_removes = float("inf")
def dfs(s, start, eval, left, right, rem):
    global ans
    global min_removes
    if start == len(s):
        if left == right:
            if rem > min_removes: return
            if rem < min_removes:
                min_removes = rem
                ans.clear()
            ans += eval[:],
        return
    
    if s[start] not in ['(', ')']:
        dfs(s, start+1, eval+s[start], left, right, rem)
    else:
        dfs(s, start+1, eval, left, right, rem+1)
        if s[start] == '(':
            dfs(s, start+1, eval+s[start], left+1, right, rem)
        else:
            if right < left:
                dfs(s, start+1, eval+s[start], left, right+1, rem)



dfs(s,0, '', 0, 0, 0)
print(ans)


    