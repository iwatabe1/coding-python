from collections import Counter, defaultdict

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
# float: 浮動小数展、小数点を含む数値
common.divider("float")
val_float = 11.03
print(val_float)
# bool: 真偽値。True / False (先頭は大文字)
positive = True
negative = False

print(positive, negative)


"""
list: 配列

sequence[start:end:step]
start: designate start place
end: designate end place
step (can be removed): designate slice step number/ default is 1
"""
common.divider("list")
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
hash_set = set()  # 定義
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
