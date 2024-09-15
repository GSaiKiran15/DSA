s = "A man, a plan, a canal: Panama"
output = ""
# for i in s:
#     if i.isalnum():
#         output += i.lower()
# print(output == output[::-1])


def alphanum(s):
    return (ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or ord('0') <= ord(s) <= ord('9'))


l = 0
r = len(s)-1

while l < r:
    while l < r and not alphanum(s[l]):
        l += 1
    while l < r and not alphanum(s[r]):
        r -= 1
    if s[l].lower() != s[r].lower():
        print(False)
        break
    else:
        l += 1
        r -= 1
print(True)
