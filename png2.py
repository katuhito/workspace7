import urllib.request

# URLと保存パスを指定
url = "https://uta.pw/shodou/img/28/214.png"
savename = "test2.png"

# ダウンロードする
mem = urllib.request.urlopen(url).read()

# ファイルへ保存
with open(savename, mode="wb") as f:
    f.write(mem)
    print("保存しました。")
