s = 'abaab'
ans = set()
def build_all_subsequences(s, seq):
    if not s:
        if seq == seq[::-1]:
            ans.add(seq)
        return
    build_all_subsequences(s[1:], seq + s[0]) 
    build_all_subsequences(s[1:], seq) 
build_all_subsequences(s, '')
print(ans)