# IP確認APIへアクセスして結果を確認する
# モジュールを取り込む
import urllib.request

# データを取得する
url = "https://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# バイナリーを文字列に変換する
text = data.decode("utf-8")
print(text)
