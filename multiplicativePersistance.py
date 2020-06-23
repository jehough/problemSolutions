from functools import reduce
def multiplicativePersistance(num):
    count = 0
    while len(str(num)) > 1:
        lst = [int(c) for c in str(num)]
        num = reduce(lambda a,b: a*b, lst)
        count += 1
    return count

print(multiplicativePersistance(123456))