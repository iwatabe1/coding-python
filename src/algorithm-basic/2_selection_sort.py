"""
Selection Sort 選択ソート
昇順、または降順にデータを並べ替える。
配列の中から最小値を見つけて、一番目の要素と入れ替える。
次に、配列の二番目以降から最小値を見つけ出して、二番目の要素と入れ替える。
繰り返し、配列を並び替える。
"""


def findSmallestItem(arr):
    min = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min:
            min = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        found_smallest_index = findSmallestItem(arr)
        sorted_arr.append(arr.pop(found_smallest_index))
    return sorted_arr


sample_arr = [i for i in reversed(range(100)) if i % 2 == 1]

print(sample_arr)
print(selectionSort(sample_arr))
