"""
1から順番にある数まで数を数えていく。
3の倍数ならFizz
5の倍数ならBuzz
両方の倍数(15の倍数)ならFizz Buzz
いずれでもなければその数を出力する。
"""


def fizzbuzz(tagert_num: int):
    for i in range(tagert_num):
        if i % (3 * 5) == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
    return None


fizzbuzz(100)
