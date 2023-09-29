def rob(values:list, n:int):
    if n == 0:
        return values[n]
    if n < 0:
        return 0
    
    pick = values[n] + rob(values, n - 2)
    notPick = rob(values, n - 1)
    return max(pick, notPick)
houses = [2, 7, 9, 3, 1]
maxValue = rob(houses, len(houses) - 1)
print(maxValue)