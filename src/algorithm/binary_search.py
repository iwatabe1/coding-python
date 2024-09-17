from bisect import bisect_left

"""
binary_search
二分探索：
リストの左端をlow, 右端をhighと定義する。

low <= high の間以下の処理を続ける。
lowとhighの真ん中の配列のインデックスをmidと定義する。
midとtargetの値を比較する。
midの値 == target
    返却
midの値 > target
    mid -1 をhighに格納し、再検査
midの値 < target
    mid +1 をlowに格納し、再検査
"""

sample_list = [i for i in range(50) if i % 2 == 1]
print(sample_list)


def binary_search(list, target):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (high + low) // 2  # 小数点切り捨て
        guess = list[mid]
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None


print(binary_search(sample_list, 0))
print(binary_search(sample_list, 1))
print(binary_search(sample_list, 15))
print(binary_search(sample_list, 48))
print(binary_search(sample_list, 50))


# 別解
def bisect_binary_search(list, target):
    res = bisect_left(list, target)
    if res != len(list):
        if target == list[res]:
            return res
        else:
            return None


print(bisect_binary_search(sample_list, 0))
print(bisect_binary_search(sample_list, 1))
print(bisect_binary_search(sample_list, 15))
print(bisect_binary_search(sample_list, 48))
print(bisect_binary_search(sample_list, 50))
