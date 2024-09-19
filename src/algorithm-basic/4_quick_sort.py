import random

"""
分割統治法：
問題全体を同じ構造の小さな問題に分割して、簡単に解けるサイズにしてから解いていく方法
1.分割する：再帰を利用して、問題を小さな問題に分割する。
2.小さな問題を解く：小さな問題を再帰的に解いていく。十分小さくなった所で解く。
3.統合する:小さな問題の部分的な解を結合して、問題全体を解く。
"""

"""
QuickSort
あるデータからランダムな要素をpivotとして選択する。
グループを分割する
    1.ピボットより小さいグループ
    2.ピボットより大きいグループ
グループが空になるか、要素が１つだけになるまで繰り返す。
"""


def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        # pivot = random.choice(arr)
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


sample_array = [random.randint(0, 100) for i in range(10)]
print(sample_array)
print(quicksort(sample_array))
