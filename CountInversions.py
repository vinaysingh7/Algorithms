#code

inversions = 0

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    
    left = mergeSort(arr[:m])
    right = mergeSort(arr[m:])
    return merge(left, right)

def merge(arr1, arr2):
    if not arr1 or not arr2:
        return arr1 if not arr2 else arr2
        
    i, j, arr = 0, 0, []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            arr.append(arr2[j])
            j += 1
            global inversions
            inversions += (len(arr1)-i)
        else:
            arr.append(arr1[i])
            i += 1
    
    if i < len(arr1):
        arr.extend(arr1[i:])
    elif j < len(arr2):
        arr.extend(arr2[j:])
        
    return arr
    
    
test_cases_count = int(input())
for _ in range(test_cases_count):
    arr_len = int(input())
    arr = [int(item) for item in input().split()]
    inversions = 0
    sorted_arr = mergeSort(arr)
    print(inversions)
    