"""
多重ループ：
10**7を超えると時間制限する。
入力サイズによっては、O(n**2)の解法を使用できる。
"""

for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                print(i, j, k, l)
