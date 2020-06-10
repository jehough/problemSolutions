from functools import reduce
from operator import xor

#my solution iterates once, bigO (n)
def find_single_among_pairs(lst):
    queue = {}
    for number in lst:
        if number in queue:
            del queue[number]
        else:
            queue[number] = True
    return list(queue.keys())[0]
            

def find_single_among_pairs_elegant(lst):
    return reduce(xor, lst)

lst = [ 2, 4, 2, 4, 5, 5, 9, 9, 7]
print(find_single_among_pairs_elegant(lst))

#udemy solution single line with xor
