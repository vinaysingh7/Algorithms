import heapq
lists = [[1, 3], [2, 4, 6], [0, 9, 10, 11]]
m = 5

def find_mth_element(lists, m):
    heap = []
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(heap, (l[0], i, 0))

    counter = 0
    while heap:
        val, list_index, index = heapq.heappop(heap)
        m -= 1
        if m == 0:
            return val
        if index+1 < len(lists[list_index]):
            heapq.heappush(heap, (lists[list_index][index+1], list_index, index+1))
    return None

ans = find_mth_element(lists, m)
print(ans)

