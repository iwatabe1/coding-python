from common_package import common

## 制御文
"""
If statement
Description: Python is special in this IF statement.
    Other many programming languages uses {} as If statement.
    But python uses : conma and 4 indent as If statement.
"""
common.divider("if statement")
# if
n = 9
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else:
    print("n is zero")

## and, or ,not
n, m = 5, 10
if n > 0 and m > 0:
    print("Both are positive.")

if n > 0 or m > 0:
    print("Either is positive.")

if not n > 0:
    print("n is not psitive.")

# range
if 0 < n <= 10:
    print("n is between 0 and 10")


"""
While statement
"""
common.divider("while")
n = 5
while n > 0:
    print(n)
    n -= 1

n = 10
while n > 0:
    n -= 1
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)  # output: 9 ,7

"""
for statement
range() function is used in For statement.
"""
common.divider("for statement")
for i in range(2):
    print(i)

for i in range(2, 3):
    print(i)

for i in range(5, 1, -1):
    print(i)

for i in reversed(range(5)):
    print(i)

# for statement can use break and continue
# if break is happenend, else will not be called
