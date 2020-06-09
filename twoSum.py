def two_sum_naive(lst, desired_sum):
    for num1 in lst:
        for num2 in lst:
            if num1+num2 == desired_sum:
                return num1, num2
        
    return None
    
    
exList = [1, 2, 3, 4, 5, 6, 7]
desired_sum = 7


def two_sum_better(lst, desired_sum):
    lst.sort()
    start = 0
    end = len(lst) - 1
    while start < end:
        current_sum = lst[start] + lst[end]
        if current_sum == desired_sum:
            return lst[start], lst[end]
        elif current_sum > desired_sum:
            end -= 1
        elif current_sum < desired_sum:
            start += 1
    return None

def two_sum_better(lst, desired_sum):
    hash_table= create_hashtable(lst)
    for num in lst:
        complement= desired_sum - num
        if complement in hash_table.keys():
            return num, complement
    return None

def create_hashtable(lst):
    hash_table = {}
    for num in lst:
        hash_table[num] = True
    return hash_table