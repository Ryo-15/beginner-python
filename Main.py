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

# coding: utf-8
# 取り込んだデータをリストに格納する

line = input().rstrip().split(",")
print(line)
print(len(line))

for enemy in line:
    print(enemy + "が現れた！")

# coding: utf-8
#英文の単語数を数える

str = "One cold rainy day when my father was a little boy he met an old alley cat on his street"
words = str.split(" ")
print(len(words))

# coding: utf-8
# 標準入力から読み込んだURLを分割する
# https://paiza.jp/cgc/users/ready

url_str = input().rstrip()
words = url_str.split("/")
print(words)

# coding: utf-8
# 複数行データをリストに格納する

# sys.stdin.readlines関数 ファイルを全て読み込み、1行毎に処理
import sys
array = []
for line in sys.stdin.readlines():
# line = input().rstrip()
    array.append(line.rstrip())
    # print(line.rstrip())

print(array)

# coding: utf-8
# 複数行のカンマ区切りデータを出力する

import sys
for line in sys.stdin.readlines():
	# ここに、文字列を分割して、出力するコードを書く
	enemy = line.rstrip().split(",")
	print(enemy[0] + "が" + enemy[1] + "匹現れた")

# coding: utf-8
# リストを使ったランダムくじ
# スライム,モンスター,ドラゴン,魔王

import random
line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")

# ランダムな数を作る範囲を調べる
num = len(line)
print("敵は" + str(num) + "匹")

# ランダムな数を生成
attack = random.randrange(num)

# 選んだ的に、「会心の一撃！」と表示
print(line[attack] + "に会心の一撃！" + line[attack] + "を倒した！")

# coding: utf-8
# じゃんけんプログラム

import random
# 標準入力から1行取得
line = input().rstrip()

# カンマで分割して、リストに代入
janken = line.split(",")

# リストの要素数を変数に代入
num = len(janken)

# リストの中身を出力
print(janken)

# ランダムに選んだリストの要素を出力
print(janken[random.randrange(num)])

# coding: utf-8
# おみくじプログラム

import random
line = input().rstrip()

# 今回は自力で全部書いてみよう！

# カンマで分割して、リストに代入
omikuji = line.split(",")

# リストの要素数を変数に代入
num = len(omikuji)

# リストの中身を出力
print(omikuji)

# ランダムに選んだリストの要素を出力
print(omikuji[random.randrange(num)])

# coding: utf-8
# Your code here!

# リストのおさらい
enemyArray = ["スライム", "モンスター", "ドラゴン"]
print(enemyArray)
print(enemyArray[0])

# 辞書の具体例
enemeyDictionary = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemeyDictionary)
print(enemeyDictionary["中ボス"])

level = "ザコ"
print(enemeyDictionary[level])

# 指定の文字を辞書にする

skills ={"職業":"戦士", "体力":100, "魔法力":200, "ゴールド":380}

print(skills)

# coding: utf-8
# Your code here!

# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])
print(len(enemies))

enemies["ザコ2"] = "メタルモンスター"
print(enemies)
print(len(enemies))

enemies["中ボス"] = "レッドドラゴン"
print(enemies)
print(len(enemies))

del enemies["ザコ"]
print(enemies)
print(len(enemies))

# coding: utf-8
# Your code here!

# 辞書をループで処理する

# 辞書のおさらい
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["中ボス"])

for rank in enemies:
    print(enemies[rank] + "が、あらわれた！")
for (rank, enemy) in enemies.items():
    print(rank + "の" + enemy + "が、あらわれた！")

# ループで辞書のキーと値を出力しよう

skills = {"職業" : "戦士", "体力" : 100, "魔法力" : 200, "ゴールド" : 380}
# この下で、ハッシュの値をループで出力してみよう
for (a, skill) in skills.items():
    print(a + "は" + str(skill) + "です")

# ループで合計を計算しよう

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for key in points:
    sum += points[key]
print(sum)


# coding: utf-8
# Your code here!

# リストの整列
weapons = ["イージスソード", "ウィンドスピア", "アースブレイカー", "イナズマハンマー"]
print(weapons)

print(sorted(weapons))
print(sorted(weapons, reverse=True))

# 数字順
weapons2 = ["4.イージスソード", "1.ウィンドスピア", "2.アースブレイカー", "3.イナズマハンマー"]
print(sorted(weapons2))

# 文字コード順になる
weapons3 = ["バーニングソード", "風神スピア", "大地ブレイカー", "稲妻ハンマー"]
print(sorted(weapons3))


#リストを逆順にソートする

apples = [310, 322, 292, 288, 300, 346]
# ここに、要素をソートして、逆順に整列し、表示するコードを記述する 
print(sorted(apples, reverse=True))


# coding: utf-8
# Your code here!

# 辞書の整列
weapons = {"イージスソード":40, "ウインドスピア":12, "アースブレイカー":99}
print(weapons)
print(sorted(weapons))
# タプル
print(sorted(weapons.items()))


# 辞書をソートして辞書で出力する
math = {"えんどう" : 99, "あだち" : 40, "いいだ" : 12}

# この下で、辞書をキーでソートして、辞書として出力しよう
print(sorted(math.items()))


# coding: utf-8
# Your code here!

# 画像用ハッシュ
item_images = {
    "剣":"http://paiza.jp/learning/images/sword.png",
    "盾":"http://paiza.jp/learning/images/shield.png",
    "回復薬":"http://paiza.jp/learning/images/potion.png",
    "クリスタル":"http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順配列
item_orders = ["クリスタル", "盾", "剣", "回復薬", "回復薬", "回復薬"]

print(item_images)
print(item_orders)

# アイテム名を取り出す
for item_name in item_orders:
    # print(item_name)
# 画像ファイル名を取り出す
    print("<img src='" + item_images[item_name] + "'>")
    print(item_name + "<br>")

# 画像用辞書
items_imges = {
    "剣" : "http://paiza.jp/learning/images/sword.png",
    "盾" : "http://paiza.jp/learning/images/shield.png",
    "回復薬" : "http://paiza.jp/learning/images/potion.png",
    "クリスタル" : "http://paiza.jp/learning/images/crystal.png"
}

# アイテムの並び順リスト
items_orders = ["剣", "盾", "回復薬", "クリスタル"]

# ここから下を記述しよう
for items_img in items_imges:
    print("<img src='" + items_imges[items_img] + "'><br>")