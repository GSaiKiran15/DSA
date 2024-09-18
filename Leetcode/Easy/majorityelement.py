nums = [2,2,1,1,1,2,2]

# Best Solution
count = 1
res = nums[0]
for i in nums[1:]:
    if count == 0:
        res = i
        count += 1
    else:
        if i == res:
            count += 1
        else:
            count -= 1
print(res)


# better than the below version

# set_nums = set(nums)

# for i in set_nums:
#     if nums.count(i) > len(nums)/2:
#         print(i)

# better than brute force

# count = 1
# nums = sorted(nums)
# target = len(nums) / 2

# if len(nums) > 1:
#     for i in range(1, len(nums)):
#         if nums[i] == nums[i-1]:
#             count += 1
#             if count > target:
#                 print(nums[i])
#                 break
#         else:
#             count = 1
# else:
#     print(nums[0])

# BRUTE FORCE

# hashmap = {}
# for i in nums:
#     hashmap[i] = 1 + hashmap.get(i, 0)
# target = len(nums) / 2
# for i in hashmap:
#     if hashmap[i] > target:
#         print(i)
#         break
