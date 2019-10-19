wood, k = [232, 124, 456], 7
wood, k = [1,2,3], 7
wood, k = [5,9,7], 4
min_val, max_val = 0, min(wood)

def validate(val, wood, k):
    c = 0
    for piece in wood:
        while val > 0 and piece >= val:
            piece -= val
            c += 1
    return c >= k

ans = 0
while min_val <= max_val:
    mid = (min_val+max_val)//2
    possible = validate(mid, wood, k)
    if possible:
        ans = mid
        min_val = mid + 1
    else:
        max_val = mid - 1
print(ans)


