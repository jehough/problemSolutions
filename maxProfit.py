def maxProfit(lst):
    profit_so_far = 0
    profit_max= 0
    for n in range(len(lst)-1):
        diff = lst[n+1] - lst[n]
        if diff < 0:
            profit_so_far = 0
        else:
            profit_so_far += diff
        if profit_so_far > profit_max:
            profit_max = profit_so_far
    return profit_max
            
price = [1, 3, 4, 5, 2, 6, 7, 8, 4]
print(maxProfit(price))