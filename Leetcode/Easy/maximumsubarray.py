nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
if len(nums) == 1:
    print(nums[0])
else:
    max_sum = nums[0]
    left = 0
    right = 1

    curr_sum = nums[left] + nums[right]
    if nums[right] > curr_sum:
        left = right
        max_sum = nums[right]
        if right + 1 <= len(nums)-1:
            right += 1
        