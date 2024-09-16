import heapq
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict, deque

from sortedcontainers import SortedDict, SortedList, SortedSet

from common_package import common

"""
str: 文字、文字列

sequence[start:end:step]
start: designate start place
end: designate end place
step (can be removed): designate slice step number/ default is 1
"""
common.divider("string")
hello_str = "HelloWorld"  # definition of Strings type
print(hello_str)

print(hello_str[0], hello_str[4])  # pick up character in Strings

print(len(hello_str))  # length of string

hello_str = hello_str + " Evrybody"  # combine
print(hello_str)

# extract characters
print(hello_str[6:8])
print(hello_str[:3])
print(hello_str[3:])
print(hello_str[::-1])

"""
int: 整数、小数点を含まない
"""
common.divider("int")
val_int = 100000000000000000000000000
print(val_int)

minus = -10000
print(minus)

sum = val_int + minus
print(sum)
"""
float: 浮動小数点、小数点を含む数値
"""
common.divider("float")
val_float = 11.03
print(val_float)
"""
bool: 真偽値。True / False (先頭は大文字)
"""
positive = True
negative = False
b = bool()
print(b)
print(positive, negative)


"""
list: 配列 Array

sequence[start:end:step]
start: designate start place. an element on this place is included.
end: designate end place. an element on this place is 'not' included.
step (can be removed): designate slice step number/ default is 1
"""
common.divider("list(Array)")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print(len(numbers))  # Length of numbers
print(numbers[0])  # show list 0
print(numbers[9])  # show list 9
print(numbers[2:4])  # show list from 2 to 4
print(numbers[:3])  # show list from first to 3
print(numbers[4:])  # show list from 4 to last
print(numbers[:])  # show all items
print(numbers[::2])  # show list devided by steps Output[1, 3, 5, 7, 9]
print(
    numbers[::-2]
)  # ステップ数にマイナスを指定すると逆順になる。 Output[10, 8, 6, 4, 2]

common.divider("list-operation")
# operation of list
numbers.append(11)
print(numbers)

numbers.pop()
print(numbers)

numbers.insert(1, 0)
print(numbers)

# check whether an element is included in the list
print(1 in numbers)
print(12 in numbers)

# empty or not
numbers = []
if numbers:  # not empty
    print("numbers is not empty")
if not numbers:  # empty
    print("numbers is empty")

## List(Array)に関するもの
"""
リスト内包表記: List comprehension
リストを生成するコードを短くする方法。
    = [<値> <繰り返し範囲> <条件(option)>]
"""
common.divider("List comprehension")
squares = [i**2 for i in range(5)]
print(squares)

squares = [i**2 for i in range(5) if i % 2 == 0]
print(squares)
"""
2次元配列 (2d Array)
"""
common.divider("2d array")
# 3 * 4の2次元配列の例
two_dim_array = [[0] * 3 for i in range(4)]
two_dim_array[0][1] = two_dim_array[1][1] = 1  # 0,1行目、2列目に1を代入
print(two_dim_array)


"""
tuple: 
    タプル。変更できない。異なるタイプの項目をグループ化するために使われる。
    定義方法: ()
"""
common.divider("tuple")
my_tuple = (1, "2")  # () で囲んで定義
print(my_tuple)
type(my_tuple)

"""
set: 
    セット: 重複を許さない、順序がない。
    定義方法: val = set(), val = {1, 2}
"""
common.divider("set")

# initizlize and add values
hash_set = set()  # 定: 注意:{} だけだとDictionary
hash_set.add(1)  # 追加
print(hash_set)
hash_set.add(2)
print(hash_set)

# initialize it by designated values
hash_set = {0, 1, 2}  # {} initialize a variable
print(hash_set)

print(1 in hash_set)  # check an extistance

hash_set.remove(2)  # 削除
print(hash_set)


"""
dictionary: 
    辞書。Hash tableとして機能する
    キーと値のペアを保存して、素早く取り出せる。
    初期化: val = {}, val = {key, value}
"""
common.divider("dictionary")

# initizlize and add values
hash_table = {}
hash_table["apple"] = 1  # {"apple", 1} のペアを設定
hash_table["orange"] = 2
print(hash_table)

# initialize it by designated values
hash_table = {"apple": 1, "banana": 2, "orange": 3}  # initialize hash table
print(hash_table)

# check extistance of value
print("apple" in hash_table)
print("grapes" in hash_table)

# remove
ret_hash_table = hash_table.pop("apple")
print(hash_table)
print(ret_hash_table)

# get value of dict
hash_table = {"apple": 1, "banana": 2, "orange": 3}  # initialize hash table

for key in hash_table:
    print(key, hash_table[key])

for val in hash_table.values():
    print(val)

for key, value in hash_table.items():
    print(key, value)

"""
defaultdict:
    辞書のサブクラス
    キーが存在しない時にデフォルトの値を生成する。
"""
common.divider("defaultdict")
# int型のデフォルト値を持つdefaultfictを作成する
hash_table = defaultdict(int)

fruits = ["apple", "banana", "apple"]

for f in fruits:
    hash_table[f] += 1

print(hash_table)

# defaultdictを利用して、リストをデフォルト値とする
hash_list = defaultdict(list)
hash_list["fruits"].append("apple")
hash_list["fruits"].append("banana")
hash_list["fruits"].append("grapes")

print(hash_list)

"""
Counter:
    辞書のサブクラス
    ハッシュ可能なオブジェクトを数えるのが得意。
"""
common.divider("Counter")
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
fruits_counter = Counter(fruits)

print(fruits_counter)

# キーを指定して出現回数を出力
print(fruits_counter["apple"])

# 最も出現回数が多い要素
most_common = fruits_counter.most_common(1)
print(most_common)

# 文字列に対して、各文字毎に出現回数をカウントする
str_counter = Counter("bananaGrapes")
print(str_counter)

"""
種類	順序がある	変更できる	重複を許可する
list    	○   	○       	○
tuple   	○   	×       	○
set     	×   	×       	×
dictionary	○ [1]	○       	×
"""

"""
キュー(Queue)
deque クラス
FIFOキューを提供する。
追加:append
左から取り出し:popleft
右から取り出し:pop
"""
common.divider("キュー(Queue)")
queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

queue.pop()
print(queue)

queue.popleft()
print(queue)

"""
ヒープ(Heap)
データ構造。特定の順序でデータを保存する。
ヒープを使うと、必ず一番優先順位が高いものを取り出すことができる(最小値)。
import heapq モジュールは最小の要素が常にルート(インデックス0)になる。
"""
common.divider("ヒープ(Heap)")
## 最小ヒープ
min_heap = []
heapq.heappush(min_heap, 4)
heapq.heappush(min_heap, 2)
heapq.heappush(min_heap, 5)
print(min_heap[0])
while min_heap:
    print(heapq.heappop(min_heap))

## 最大ヒープ。値をネガティブにして実現する
## heapqには最大ヒープを実現する機能はない
max_heap = []
heapq.heappush(max_heap, -4)
heapq.heappush(max_heap, -2)
heapq.heappush(max_heap, -5)

print(-max_heap[0])

while max_heap:
    print(heapq.heappop(max_heap))

"""
ソート(Sorting)
sorted(): デフォルトは昇順のソート
sort(): メソッド。引数とソートの順番を指定できる。
    破壊的メソッドなので、元の配列が書き換えられる。
    降順: reverse=True
"""
common.divider("ソート(Sorting)")
# 昇順
numbers = [3, 7, 5, 2, 4, 8, 5]
sorted_nums = sorted(numbers)
print(sorted_nums)

# 降順
numbers.sort(reverse=True)
print(numbers)

numbers.sort()
print(numbers)


## 文字列 辞書順にソートする
fruits = ["orange", "apple", "banana", "grape"]
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

## ソート基準のカスタマイズ
## リストの文字列の長さでソートをする場合
fruits.sort(key=lambda x: len(x))
print(fruits)


## 複数の要素でソートする
## tupleを使用すれば、最初の要素から順に比較してソートされる。
## 例えば出現回数順 -> 辞書順でソートしたい時などに使える。
## list, heapq などでも同様の結果が得られる。
vers = [(1, 2, 3), (1, 2, 2), (1, 1, 2)]
vers.sort()
print(vers)

vers = [(1, 2, 3), (1, 2, 2), (1, 1, 4)]
vers.sort()
print(vers)


# 数字と文字の組み合わせでも。
money_fruits = [(200, "grapes"), (100, "grapes"), (200, "banana")]
money_fruits.sort()
print(money_fruits)

"""
bisect
二分探索 binary_search
"""

nums = [1, 2, 3, 4, 7, 7, 7, 7, 8, 12, 35]
# 値 7 を二分探索して、見つかった複数の7の内、最小(左端)のインデックスを返す
# numsにおいて値が7のlower bound(7以上の数字が出現する中での最小のインデックス)
print(bisect_left(nums, 7))

# 値 7 を二分探索して、見つかった複数の7の内、最大(右端) + 1 のインデックスを返す
# numsにおいて値が7のupper bound + 1 (7より大きい数字が出現する中での最小のインデックス)
print(bisect_right(nums, 7))

print(bisect_left(nums, 13))
print(bisect_right(nums, 13))

"""
Sorted Containers
"""
# SortedSet
# 常にソートされた Set のデータ構造
sorted_set = SortedSet([3, 3, 1, 1, 5, 2])
print(sorted_set)

sorted_set.add(4)  # 追加
print(sorted_set)
sorted_set.add(3)  # 同じ値は追加されない。
print(sorted_set)
sorted_set.discard(3)  # 削除
print(sorted_set)
print(sorted_set.bisect_left(2))
print(sorted_set.bisect_right(2))


# SortedList
# 常にソートされたList のデータ構造。重複が許容される。
sorted_list = SortedList([3, 1, 5, 2])
print(sorted_list)  # SortedList([1, 2, 3, 5])

# O(logN)
sorted_list.add(5)
print(sorted_list)  # SortedList([1, 2, 3, 5, 5])
sorted_list.add(4)
print(sorted_list)  # SortedList([1, 2, 3, 4, 5, 5])

print(sorted_list.bisect_left(3))
print(sorted_list.bisect_right(3))

# SortedDict
# Dict の要素がソートされている
sorted_dict = SortedDict({"apple": 300, "oragne": 200, "banana": 100})

print(sorted_dict)  # SortedDict({'apple': 300, 'banana': 100, 'oragne': 200})

print(sorted_dict.items())
print(sorted_dict.keys())
print(sorted_dict.values())

for k, v in sorted_dict.items():
    print(k)
    print(v)
