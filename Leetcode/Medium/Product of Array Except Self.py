def productExceptSelf(self, nums):
    output = []
    total_product = 1
    zero_count = 0
    zero_index = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_count += 1
            zero_index = i
        total_product *= nums[i]
    if zero_count == 1:
        total_product = 1
        for i in range(len(nums)):
            if i != zero_index:
                total_product *= nums[i]
        output = [0] * len(nums)
        output[zero_index] = total_product
    else:
        for i in range(len(nums)):
            if nums[i] != 0:
                output.append(int(total_product / nums[i]))
            else:
                output.append(0)
    return output