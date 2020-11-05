# coding: utf-8
#HTMLを表示する
print("<h1>hello world</h1>")
print("<p>世界のみなさん")
print("<b>こんにちは</b></p>")

# coding: utf-8
# 変数を使う
player = "戦士"
print(player + "は、荒野を歩いていた")
print(player + "は、モンスターと戦った")
print(player + "は、モンスターをたおした")

# coding: utf-8
#数の表示とサイコロ
import random
number = random.randint(1, 100)
print("スライムが" + str(number) + "匹現れた")

# coding: utf-8
# 計算する
number = 100 + 40
print(number + 30 * 3)
print(number)

# coding: utf-8
#値段を計算する
#apple_price	リンゴの単価
#apple_num	リンゴを買う数
import random
apple_price = 350
apple_num = random.randint(1, 10)
print("リンゴの単価：" + str(apple_price) + "円")
print("リンゴを買う数：" + str(apple_num) + "個")
total = apple_price * apple_num
print("合計金額：" + str(total) + "円")

# coding: utf-8
# データの種類
number = 100 + 40	#数値
strings = "ハロー" + "paiza"	#文字列
print(number)
print(strings)
print(str(number) + strings)

# coding: utf-8
# if文による条件分岐
number = 1
if number == 1:
    print("スキ！")
else:
    print("キライ")

    # coding: utf-8
# if文による条件分岐　elif文
number = 3
if number == 1:
	print( "スキ！")	#条件式が成立したときの処理
elif number == 2:
    print("どちらでもない")
else:
	print( "キライ")	#条件式が成立しなかったときの処理

# coding: utf-8
# if文による条件分岐　比較演算子
time= 13
if time < 12:
	print("午前中")	#条件式が成立したときの処理
elif time == 12:
    print("正午")
elif time > 12:
    print("午後")

# coding: utf-8
# おみくじを作る
# 比較演算子 == > < >= <= !=
# 大吉  中吉  小吉  凶  大凶
import random
omikuji = random.randint(1, 10)
print(omikuji)

if omikuji == 1:
    print("大吉")
elif omikuji == 2:
    print("中吉")
elif omikuji <= 4:
    print("小吉")
elif omikuji <= 7:
    print("凶")
else:
    print("大凶")

# coding: utf-8
# RPGのクリティカルヒットを再現
# 比較演算子 == > < >= <= !=

# スライムと戦っている。
# 1から10のサイコロをふって、
# 6未満の場合、サイコロの目だけダメージを与えたと表示。
# 6以上の場合、クリティカルヒットとして、100のダメージを与えたと表示。
import random
hit = random.randint(1, 10)
# print(hit)

if hit < 6:
    print("スライムに" + str(hit) + "のダメージを与えた！")
else:
    print("クリティカルヒット！スライムに100のダメージを与えた！")

# coding: utf-8
# 西暦年から平成年を求める
import datetime
seireki = datetime.date.today().year
print("西暦" + str(seireki) + "年は、",end="")

heisei = seireki - 1988
print("平成" + str(heisei) + "年です。")

# coding: utf-8
# for inによるループ処理

for i in range(6, 11):
    print("hello world:" + str(i))
print("last " + str(i))

# coding: utf-8
# whileによるループ処理

i = 1
while i <= 10:
    print(i)
    i = i + 1
    print("next:" + str(i))
print("last" + str(i))

# coding: utf-8
# whileによるループ処理

i = 10# カウンタ変数を初期化
while i >= 1:
    print(i)  # 繰り返し処理
    # i = i + 1 # カウンタ変数を更新
    i -= 1
print("last:" + str(i))

import random
hp = 30
while hp > 0:
    hit = random.randint(1, 10)
    print("スライムに" + str(hit) + "のダメージを与えた！")
    hp -= hit
print("スライムを倒した")

# coding: utf-8
# 年齢入力のプルダウン作成
print("<select name=\'age\'>")
# print("<option>1才</option>")
# print("<option>2才</option>")
# print("<option>3才</option>")
for age in range(100):
    print("<option>" + str(age + 1) + "歳</option>")
print("</select>")

# coding: utf-8
# inputによる入力処理
line = input()
print("hello" + line)

# coding: utf-8
# 標準入力とループ処理
# line = input()
# print("hello " + line)

count = int(input())
# print("データ個数 " + str(count))
for i in range(count):
    line = input().rstrip()
    print(line + "は、スライムを攻撃した！")

# coding: utf-8
# 標準入力とループ処理
a = int(input())
b = int(input())

for i in range(a, b + 1):
  print(i)

# coding: utf-8
# 西暦年と平成年の対応表を作る
# 1989年から2016年までをループで出力
# ループ内で、各西暦年を平成年に変換
for seireki in range(1989, 2020):
    print("西暦" + str(seireki) + "年は、", end = "")
    heisei = seireki - 1989
    print("平成" + str(heisei) + "年です。")

# coding: utf-8
# 特定期間の西暦年と昭和年の対応表を作る
# 1行目：開始年
# 2行目：期間
# 昭和年 = 西暦年 - 1925
# 出力：西暦XXXX年は昭和YY年です
start = int(input())
term = int(input())

for seireki in range(start, start + term):
    print("西暦" + str(seireki) + "年は", end = "")
    syowa = seireki - 1925
    print("昭和" + str(syowa) +"年です")

# coding: utf-8
# リストを作成する
player_1 = "勇者"
player_2 = "魔法使い"

print(player_1)
print(player_2)

team = ["勇者", "魔法使い"]
print(team)

# coding: utf-8
# リストの要素を取り出す

team = ["勇者", "魔法使い"]
print(team)
print(team[0])
num = 0
print(team[num + 1])
print(len(team))

# coding: utf-8
# リストの要素を操作する

team = ["勇者", "魔法使い"]
print(team)
print(team[0])
print(len(team))

team.append("戦士")
print(team)
print(len(team))

team[2] = "ドラゴン"
print(team)
print(len(team))

team.pop(2)
print(team)
print(len(team))

# coding: utf-8
# ループでリストを操作する

team = ["勇者", "戦士", "魔法使い", "盗賊"]
print(team)
print(team[0])

for i in range(5):
    print(i)
    
print("<select name='job'>")
for job in team:
    print("<option>" + job + "</option>")
print("</select>")


