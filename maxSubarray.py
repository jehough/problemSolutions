def maxSubArray(array, k):
    for i in range(len(array)):
        if i < len(array) - 2:
            print(max([array[i], array[i+1], array[i+2]]))

maxSubArray([3, 4, 2, 1, 5, 3, 7], 3)