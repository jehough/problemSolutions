def permutations(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    all_permutations = []
    for i in range(0, len(lst)):
        reminder_list = lst[:i] + lst[i+1:]
        for p in permutations(reminder_list):
            all_permutations.append([lst[i]]+p)
            
    return all_permutations
input_list = [1,2,3]
for p in permutations(input_list):
    print(p)
