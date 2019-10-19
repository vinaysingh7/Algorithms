import heapq
nums = [1, 6, 1, 1, 1, 1, 7]

def max_appeal():
    heap = []
    heap[0] = nums[0] + nums[0]
    
    heapq.heapify(heap)
    for i, num in enumerate(nums[1:]):
        if num+i > heap[0]
