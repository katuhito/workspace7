# !/usr/bin/env python3

# コマンドライン引数を得る
import sys
import urllib.request as req
import urllib.parse as parse

# パラメーターをURLエンコードする
if len(sys.argv) <= 1:
    print("USAGE: hyakunin.py (keyword)")
    sys.exit()
keyword = sys.argv[1]

API = "https://api.aoikujira.com/hyakunin/get.php"
query = {
    "fmt": "ini",
    "key": keyword
}
params = parse.urlencode(query)
url = API + "?" + params
print("url=", url)

# ダウンロード
with req.urlopen(url) as r:
    b = r.read()
    data = b.decode('utf-8')
    print(data)
