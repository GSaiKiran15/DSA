nums = [-1, 0, 3, 5, 9, 12]
target = 12

l = 0
r = len(nums)-1

while l <= r:
    mid = (r + l) // 2
    if nums[mid] == target:
        print(mid)
        break
    elif nums[mid] < target:
        l = mid + 1
    else:
        r = mid - 1
print(-1)
