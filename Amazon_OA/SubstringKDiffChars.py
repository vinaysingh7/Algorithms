s = "awaglknagawunagwkwagl"
k = 4

i, j,  seen = 1, 0, {s[0]}
ans = set()
while i < len(s):
    while j < i and s[i] in seen:
        seen.remove(s[j])
        j += 1
    while len(seen) >= k:
        seen.remove(s[j])
        j += 1
    seen.add(s[i])
    if len(seen) ==4:
        ans.add(s[j:i+1])
    i += 1
print(ans)
print(len(ans))

