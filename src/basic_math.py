import math

from common_package import common

common.divider("割り算")
# 割り算
print(5 / 2)  # floatになる
print(5 // 2)  # 小数点以下切り捨て

common.divider("剰余算")
# 剰余算
print(5 % 3)  # 2
print(-5 % 3)  # 符号を保持しない結果を返す

print(math.fmod(-5, 3))  # 符号を保持した結果を返す

common.divider("Math関数")
# Math functions
print(math.floor(5 / 2))  # 引数以下の最大の整数返す 2
print(math.ceil(5 / 2))  # 引数以上の最小の整数を返す 3
print(math.sqrt(2))  # 平方根
print(math.pow(2, 3))  # べき乗
print(2**3)  # べき乗

common.divider("無限大")
# 無限大の表現 Infinity expression
# float("inf")
# float("-inf")
p = math.pow(2, 100)
print(p)
print(math.pow(2, 100) < float("inf"))
