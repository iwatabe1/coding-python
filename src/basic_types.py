
def divider(divider_name: str):
    """
    Putting section divider for visibility

    Prameters
    ---------
    args: str
        Divider name.
    
    Returns
    -------
    res: str
        Combined divider name.
    """
    res = "====================" + divider_name + "===================="
    return print(res)

"""
str: 文字、文字列

sequence[start:end:step]
start: designate start place
end: designate end place
step (can be removed): designate slice step number/ default is 1
"""
divider("string")
str = "HelloWorld" # definition of Strings type
print(str)

print(str[0],str[4]) # pick up character in Strings

print(len(str)) # length of string

str = str + " Evrybody" # combine
print(str)

# extract characters
print(str[6:8])
print(str[:3])
print(str[3:])
print(str[::-1])

"""
int: 整数、小数点を含まない
"""
divider("int")
int = 100000000000000000000000000
print(int)

minus = -10000
print(minus)

sum = int + minus
print(sum)
# float: 浮動小数展、小数点を含む数値
divider("float")
float = 11.03
print(float)
# bool: 真偽値。True / False (先頭は大文字)
true = True
false = False

print(true, false)


"""
list: 配列

sequence[start:end:step]
start: designate start place
end: designate end place
step (can be removed): designate slice step number/ default is 1
"""
divider("list")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

print(len(numbers)) # Length of numbers
print(numbers[0]) # show list 0
print(numbers[9]) # show list 9
print(numbers[2:4]) # show list from 2 to 4
print(numbers[:3]) # show list from first to 3
print(numbers[4:]) # show list from 4 to last
print(numbers[:]) # show all items
print(numbers[::2]) # show list devided by steps Output[1, 3, 5, 7, 9]
print(numbers[::-2]) #ステップ数にマイナスを指定すると逆順になる。 Output[10, 8, 6, 4, 2]

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
if numbers: # not empty
    print("numbers is not empty")
if not numbers: # empty
    print("numbers is empty")

"""
tuple: 
    タプル。変更できない。異なるタイプの項目をグループ化するために使われる。　
"""
divider("tuple")
my_tuple = (1, "2") # () で囲んで宣言
print(my_tuple)
type(my_tuple)

"""
set: 
    セット: 重複を許さない、順序がない。
"""
divider("set")
hash_set = set()
hash_set.add(1)
print(hash_set)
hash_set.add(2)
print(hash_set)


"""
dictionary: 
    辞書。他の言語では map?

"""
divider("dictionary")
"""
種類	順序がある	変更できる	重複を許可する
list    	○   	○       	○
tuple   	○   	×       	○
set     	×   	×       	×
dictionary	○ [1]	○       	×
"""