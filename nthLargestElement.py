import heapq

#my simple answer
def tenth_largest_element(arr):
    arr.sort()
    return arr[-10]
    
# best solution
def largest_element(arr, n):
    min_heap = []
    for i in range(0, n):
        heapq.heappush(min_heap, arr[i])
    for num in arr[n:]:
        heapq.heappushpop(min_heap, num)
    return heapq.heappop(min_heap)

arr = [1, 8 , 3, 5, 2, 0 ,5 ,6, 10, 11, 12, 21]
print(tenth_largest_element(arr))

print(largest_element(arr, 10))
