# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ay
from collections import deque

N = int(input())
queries = [input().split() for i in range(N)]

S = deque()
for q in queries:
    if q[0] == "1":
        S.append(q[1])
    if q[0] == "2":
        print(S[-1])
    if q[0] == "3":
        S.pop()
