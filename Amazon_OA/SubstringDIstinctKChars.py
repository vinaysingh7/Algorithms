s, k = "pqpqs", 2
n = len(s)
i, j = 0 , 1
distinct = {s[0]}
ans = 0
prefix = 0
while j < n:
    if s[j] in distinct: prefix+= 1
    distinct.add(s[j])
    print(j, i, distinct)
    if len(distinct) > k:
        i = j
        distinct = {s[j]}
        prefix = 0
        while i >= 0 and len(distinct) < k:
            i -= 1
            if s[i] in distinct: prefix += 1
            distinct.add(s[i])
        print(distinct, ans, i, j)
    j += 1
    if len(distinct) == k:
        ans += 1 + prefix
print(ans)



    