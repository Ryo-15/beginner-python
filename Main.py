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