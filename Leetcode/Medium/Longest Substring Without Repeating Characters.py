s = "dvdf"
def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        count = 0
        h = {}
        l = 0
        a = True
        if len(s) <= 1:
            return len(s)
        while a:
            for i in range(l, len(s)):
                if s[i] not in h:
                    h[s[i]] = i
                    count += 1
                    output = max(output, count)
                elif s[i] in h:
                    count = 0
                    l = h[s[i]] + 1
                    h = {}
                    break
                if i == len(s)-1:
                    a = False
                    break
        return output


# for i in s:
#     if i not in h:
#         h[i] = 1
#         count += 1
#         output = max(output,count)
#     elif i in h:
#         # if count > output:
#         #     output = count
#         count = 1
# if output == 0:
#     output = count
# print(output)