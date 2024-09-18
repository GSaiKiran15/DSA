nums = [3, 0, 1]
sum, est_sum = 0, 0
for i in nums:
    sum += i
for i in range(1, len(nums)+1):
    est_sum += i
print(est_sum - sum)
