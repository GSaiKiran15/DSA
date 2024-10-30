nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
m = 3
nums2_last_pointer = -1
num1_last_pointer = -1
value_pointer = len(nums1) - m - 1

for i in range(len(nums1)):
    if nums1[value_pointer] <= nums2[nums2_last_pointer]:
        nums1[num1_last_pointer] = nums2[nums2_last_pointer]
        nums2_last_pointer -= 1
    else:
        nums1[num1_last_pointer] = nums1[value_pointer]
        value_pointer -= 1
print(nums1)
