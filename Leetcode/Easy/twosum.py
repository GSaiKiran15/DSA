nums = [3, 3]
target = 6

hashmap = {}

for i, j in enumerate(nums):
    if target - j in hashmap and hashmap[target-j] != i:
        print([hashmap[target-j], i])
    else:
        hashmap[j] = i

print(hashmap)
