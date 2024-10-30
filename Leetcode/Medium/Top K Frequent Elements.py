nums = [1, 1, 1, 2, 2, 3, 4, 4, 4]
k = 2
count = {}
freq = [[] for i in range(len(nums) + 1)]

for i in nums:
    count[i] = 1+count.get(i, 0)

for n, c in count.items():
    freq[c].append(n)

output = []

for i in range(len(freq) - 1, 0, -1):
    for j in freq[i]:
        output.append(j)
        if len(output) == k:
            print(output)
