def two_sum(a, target):
    a.sort()
    n = len(a)
    i, j = 0, n-1
    ans = 0
    while i < j and i < n and j >= 0:
        s = a[i] + a[j]
        print("here", ans, s, target)
        if s < target:
            i += 1
        elif s > target:
            j -= 1
        else:
            ans += 1
            i += 1
            j -= 1
            while i+1 < n and a[i] == a[i-1]:
                i += 1
            while j >= 0 and a[1] == a[j+1]:
                j -= 1
    return ans
nums, target = [1, 1, 2, 45, 46, 46], 47
nums, target = [1, 1], 2
nums, target = [1, 5, 1, 5], 6
print(two_sum(nums, target))
        
