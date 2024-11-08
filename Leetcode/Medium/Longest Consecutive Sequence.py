nums = [1,2,0,1]

numSet = set(nums)
longest = 0

# for n in nums:
#     if (n-1) not in numSet:
#         length = 0
#         while (n + length) in numSet:
#             length += 1
#         longest = max(longest, length)
# print(longest)

length = 1
for n in nums:
    while (n-length) in numSet:
        length += 1
    longest = max(longest, length)
print(longest)

# if len(nums) < 2:
#     print(len(nums))
# else:
#     nums.sort()
#     l = 0
#     r = 1
#     max_count = 0
#     count = 1
#     while r <= len(nums)-1:
#         if nums[r] == nums[l] + 1:
#             count += 1
#         elif nums[r] > nums[l] + 1:
#             max_count = max(max_count, count)
#             count = 1
#         elif nums[r] == nums[l]:
#             l += 1
#             r += 1
#             continue
#         l += 1
#         r += 1
#     max_count = max(max_count, count)
# print(max_count)