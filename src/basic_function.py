# 関数の定義(Function)
def hello(name):
    print(f"Hello, {name}!")


hello("man")


"""
内部関数(Inner function)
関数の内部に別の関数を定義することができる。(内部関数、ネスト関数とも呼ぶ)
内部関数から、外部関数の変数にアクセスできる。
"""


def outer_function(x):
    def inner_function(y):
        return x + y  # inner function can access to outer variable as like x

    return inner_function(3)


print(outer_function(5))
