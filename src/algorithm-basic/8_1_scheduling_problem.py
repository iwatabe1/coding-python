"""
8_貪欲法
各ステップで最適な手を選ぶ。

8_1_scheduling_problem
大学の授業をできるだけ多く取りたい。
時間割に対して最適な取得の方法は？
データ構造：
N: 行数
|授業名|開始時刻|終了時刻|
英語 09:00 10:00
数学 09:30 10:30
国語 10:00 11:00
音楽 10:30 11:30
情報 11:00 12:00

解法:
1.最短で終了する授業を選ぶ
2.最初の授業の後に始まる授業を選ぶ
3.繰り返す。
"""

# python ./src/algorithm-basic/8_1_scheduling_problem.py < ./src/algorithm-basic/8_1_input.txt
