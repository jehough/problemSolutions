from collections import deque
# My original solution (doesn't take into account space of k)
def maxSubArray(array, k):
    for i in range(len(array)):
        if i < len(array) - 2:
            print(max([array[i], array[i+1], array[i+2]]))

maxSubArray([3, 4, 2, 1, 5, 3, 7], 3)

# Solution from Daily Coding Problems
def max_of_subarrays(lst, k):
    q = deque()
    for i in range(k):
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)

    # Loop invariant: q is a list of indices where their corresponding values are in descending order.
    for i in range(k, len(lst)):
        print(lst[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and lst[i] >= lst[q[-1]]:
            q.pop()
        q.append(i)
    print(lst[q[0]])