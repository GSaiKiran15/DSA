nums = [1, 2, 1, 2, 4]

hashmap = {}

for i in nums:
    hashmap[i] = 1 + hashmap.get(i, 0)
for i in hashmap:
    if hashmap[i] == 1:
        print(i)
res = 0
for n in nums:
    res = n ^ res
    print(n, n ^ res, res)
print(res)
