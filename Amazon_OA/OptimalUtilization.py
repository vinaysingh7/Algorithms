def optimal_utilization(a, b, target):

    a.sort(key=lambda x: (x[1], x[0]))
    b.sort(key=lambda x: (x[1], x[0]))
    m, n = len(a), len(b)
    i, j = 0, n-1
    diff = float("inf")
    ans = []
    while i < m and j >= 0:
        summed = a[i][1] + b[j][1]
        if target - summed >= 0:
            if diff > target - summed:
                diff = target - summed
                ans.clear()
            ans += [a[i][0], b[j][0]],
            temp = j
            while temp > 0 and b[temp][1] == b[temp-1][1]:
                temp -= 1
                ans += [a[i][0], b[temp][0]],
            i += 1
        else:
            j -= 1
    print("a = ",a,"b = ", b)
    print("ans:", ans)
    print()
    return ans
l = [ 
        [ [[1, 2], [2, 4], [3, 6]], [[1, 2]], 7 ], 
        [ [[1, 3], [2, 5], [3, 7], [4, 10]],  [[1, 2], [2, 3], [3, 4], [4, 5]], 10 ],
        [ [[1, 8], [2, 7], [3, 14]], [[1, 5], [2, 10], [3, 14]], 20 ],
        [ [[1, 8], [2, 15], [3, 9]], [[1, 8], [2, 11], [3, 12]], 20 ],
        [ [[1, 5], [2, 5]], [[1, 5], [2, 5]], 10 ]
    ]
for a, b, target in l:
    optimal_utilization(a, b, target)
