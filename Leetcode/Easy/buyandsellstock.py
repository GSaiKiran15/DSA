prices = [1, 2, 4]

# Best Solution
left = 0
right = 1
max_profit = 0

while right < len(prices):
    if prices[left] < prices[right]:
        profit = prices[right] - prices[left]
        max_profit = max(max_profit, profit)
    else:
        left = right
    right += 1
print(max_profit)
