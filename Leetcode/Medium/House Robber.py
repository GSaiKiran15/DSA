nums = [1, 2, 3, 1]
odd_pointer = 1
even_pointer = 0
if len(nums) <= 1:
    print(False)
odd_sum = 0
even_sum = 0
for i in range(len(nums)):
    if i % 2 == 0:
        even_sum += nums[i]
    else:
        odd_sum += nums[i]
print(max(odd_sum, even_sum))
