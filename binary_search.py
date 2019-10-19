def binary_search(l, r, arr, item):
    ans = -1
    while l <= r:
        mid = (l+r)//2
        print("mid", mid, arr[mid])
        if arr[mid] < item:
            l = mid+1
        elif arr[mid] > item:
            print("hrere2")
            ans = mid
            r = mid -1
        else:
            return mid
    return ans
        

arr = [2,7,9,13,25,56]
index = binary_search(0, len(arr)-1, arr, 24)
print(index)
print(arr[index])