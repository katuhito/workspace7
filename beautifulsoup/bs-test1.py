from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">スクレイピングとは？</h1>
    <p id="body">Webページから任意のデータを抽出すること</p>
</body></html>
"""

# HTMLを解析する
soup = BeautifulSoup(html, 'html.parser')

# 任意の部分を抽出する
h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 要素のテキストを表示する
print("h1 = " + h1.string)
print("p = " + p1.string)
print("p = " + p1.string)
