import collections


class Solution:
    def isValid(self, s: str) -> bool:
        opens = {"(", "{", "["}
        closes = {")", "}", "]"}

        stack = collections.deque([])

        for i in range(len(s) - 1):
            val = s[i]
            if val in opens:
                stack.append(val)
            elif val in closes:
                if stack.count == 0:
                    break
                else:
                    st = stack.pop()
