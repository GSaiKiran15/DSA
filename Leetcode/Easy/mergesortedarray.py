# nums1 = [0,0,0,0,0]
# nums2 = [1,2,3,4,5]
# m = 0
# n = 5

# last = m + n - 1
# while m > 0 and n > 0:
#     if nums1[m-1] > nums2[n-1]:
#         nums1[last] = nums1[m-1]
#         m -= 1
#     else:
#         nums1[last] = nums2[n-1]
#         n -= 1
#     last -= 1

# while n > 0:
#     nums1[last] = nums2[n-1]
#     n, last = n-1, last - 1

nums = [3,2,2,3]
val = 3

output = 0
for i in range(-1, len(nums), 1):
    print(i)
    # if nums[i] == val:
    #     output += 1
    #     nums.pop(i)