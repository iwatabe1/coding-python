"""
クラスClass
Pythonにおけるコンストラクタは __init__ メソッド。インスタンス生成時に自動的に呼び出される。
インスタンスメソッド:クラス内部で定義された関数。
    メソッドの最初の引数は self 、メソッドを呼び出したインスタンスそのものを示す。
"""


class MyClass:
    # constructor method
    def __init__(self, name) -> None:
        self.name = name

    # instance method
    def hello_world(self):
        print(f"Hello, {self.name}")


obj = MyClass("sample")
obj.hello_world()
