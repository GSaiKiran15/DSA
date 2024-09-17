from collections import Counter

s = "anagram"
t = "nagaram"

print(sorted(s) == sorted(t))

print(Counter(s) == Counter(t))

hash_s, hash_t = {}, {}

for i in range(len(s)):
    hash_s[s[i]] = 1 + hash_s.get(s[i], 0)
    hash_t[t[i]] = 1 + hash_t.get(t[i], 0)
for i in s:
    if hash_s[i] != hash_t.get(i):
        print(False)
print(True)
