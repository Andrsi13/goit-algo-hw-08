import heapq



def merge_k_lists(lists):
    
    min_heap = []

    for list in lists:
        for el in list:
            heapq.heappush(min_heap, el)
    print(min_heap)

    result = []

    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result


lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
