matrix = [[1,2,3,4], [2, 3, 4, 5], [1,2,3,4],[4,3,2,1]]

def matrixSpiral(matrix):
    if len(matrix) == 0:
        return None
    for num in matrix[0]:
        print(num)
    matrix.remove(matrix[0])
    for arr in matrix:
        print(arr.pop())
    matrix[-1].reverse()
    for num in matrix[-1]:
        print(num)
    matrix.pop()
    matrix.reverse()
    for arr in matrix:
        print(arr.pop(1))
    matrix.reverse()
    matrixSpiral(matrix)
    
matrixSpiral(matrix)