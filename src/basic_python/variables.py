"""
Basic variable explanation on Python
"""

# declaration and re assingment
n = 0
print(n)
n = "ABC"
print(n)

# assigment multiple variables from multi inputs
a, b = 1, 2
print(a, b)

# swap 入れ替え
a, b = b, a
print(a, b)

# 複数の変数に一括で同じ値の代入
a = b = c = 0
print(a, b, c)

# increment, decrement
a += 1  # not acceptable ++a and a++ expression
b -= 1

# None (Null)
n = None
print(n)
