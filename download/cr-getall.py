# 再帰的処理
# モジュール取り込み
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as parse
from urllib.parse import urlparse
from os import makedirs
import os.path, time, re

# 処理済み判断変数
proc_files = {}

# HTML内にあるリンクを抽出する関数
def enum_links(html, base):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.select("link[rel='stylesheet']")
    links += soup.select("a[href]")
    result = []
    # href属性を取り出し、リンクを絶対パスに変換
    for a in links:
        href = a.attrs['href']
        url = urljoin(base, href)
        result.append(url)
    return result

# ファイルをダウンロードして保存する関数
def download_file(url):
    o = urlparse(url)
    savepath = "./" + o.netloc + o.path
    if re.search(r"/$", savepath):  #ディレクトリーならindex.html
        savepath += "index.html"
    savedir = os.path.dirname(savepath)
    # すでにダウンロード済み?
    if os.path.exists(savepath):
        return savepath
    # ダウンロード先のディレクトリーを作成
    if not os.path.exists(savedir):
        print("mkdir=", savedir)
        makedirs(savedir)
        # ファイルをダウンロード
    try:
        print("download=", url)
        urlretrieve(url, savepath)
        time.sleep(1)  #礼儀として1秒スリーブ
        return savepath
    except:
        print("ダウンロード失敗：", url)
        return None

# HTMLを解析してダウンロードする関数
def analize_html(url, root_url):
    savepath = download_file(url)
    if savepath is None:
        return
    if savepath in proc_files:
        return   #解析済みなら処理しない
    proc_files[savepath] = True
    print("analize_html=", url)
    # リンクを抽出
    html = open(savepath, "r", encoding="utf-8").read()
    links = enum_links(html, url)
    for link_url in links:
        # リンクがルート以外のパスを指していたら無視する
        if link_url.find(root_url) != 0:
            if not re.search(r".css$", link_url):
                continue
        # HTMLかどうか？
        if re.search(r".(html|htm)$", link_url):
            # 再帰的にファイルを解析
            analize_html(link_url, root_url)
            continue
        # それ以外のファイル
        download_file(link_url)

if __name__ == "__main__":
    # URLをまるごとダウンロード
    url = "https://etama.jp/906/"
    analize_html(url, url)
