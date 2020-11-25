import random

# BMIを計算して体型を出す
def calc_bmi(h, w):
    bmi = w / (h/100) * 2
    if bmi < 18.5: return "thin"
    if bmi < 25: return "nomal"
    return "fat"

# 出力ファイルの準備
fp = open("bmi.csv", "w", encoding="utf-8")
fp.write("height, weight, label\r\n")

# ランダムなデータを生成
cnt = {"thin":0, "nomal":0, "fat":0}
for i in range(20000):
    h = random.randint(120, 200)
    w = random.randint(35, 80)
    label = calc_bmi(h, w)
    cnt[label] += 1
    fp.write("{0},{1},{2}\r\n".format(h, w, label))
fp.close()
print("ok,", cnt)
