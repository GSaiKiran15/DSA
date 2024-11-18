nums = [0,1,0,3,12]
l = 0
r = 1
while r <= len(nums)-1:
    if nums[l] == 0:
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], 0
            l += 1
            r += 1
        else: 
            r += 1
    else:
        l += 1
        r += 1
print(nums)