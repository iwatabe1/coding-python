import math
from collections import deque

S = input()

dict = {S: 0}

queue = deque([S])
ans = 0

while len(queue):
    current = queue.popleft()

    if current == "atcoder":
        ans = dict.get(current)
        break

    for i in range(1, 7):
        next = list(current)
        next[i], next[i - 1] = next[i - 1], next[i]
        nextStr = "".join(next)
        if dict.get(nextStr) is None:
            queue.append(nextStr)
            dict[nextStr] = dict.get(current) + 1

print(ans)
