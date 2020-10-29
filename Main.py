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
