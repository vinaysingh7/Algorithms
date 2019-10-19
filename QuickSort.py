def partition(nums, l, r):
    pivot = nums[r]
    i = l
    for j in range(l, r):
        if pivot > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[r], nums[i] = nums[i], nums[r]
    print(pivot, nums[r])
    return i


def QuickSort(nums, l, r):
    if l >= r:
        return
    p = partition(nums, l, r)
    QuickSort(nums, l, p-1)
    QuickSort(nums, p+1, r)
nums = [5,1]
QuickSort( nums, 0, len(nums)-1)
print(nums)
