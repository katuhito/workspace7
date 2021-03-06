import scrapy, pprint

class Soseki4Spider(scrapy.Spider):
    name = 'soseki4'
    allowed_domains = ['www.aozora.gr.jp']
    # 夏目漱石の作品一覧ページ
    start_urls = ['https://www.aozora.gr.jp/index_pages/person148.html']

    def parse(self, response):
        li_list = response.css('ol > li a')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)
            # 図書カードのページ取得を指示
            yield response.follow(
                href2, self.parse_card
            )

    # 図書カードのページ解析
    def parse_card(self, response):
        title = response.css('title::text').extract_first()
        # ダウンロード先ZIPファイルの取得
        alist = response.css('table.download tr td a')
        for a in alist:
            href = a.css('::attr(href)').extract_first()
            href2 = response.urljoin(href)
            if href2[-4:] != ".zip": continue
            # ダウンロードを指示する
            req = scrapy.Request(href2, callback=self.parse_item)
            req.meta["title"] = title
            yield req

    # ZIPファイルの保存
    def parse_item(self, response):
        # メタ情報よりファイル名を決定
        title = response.meta["title"]
        title = title.replace('図書カード：', '').strip()
        fname = title + '.zip'
        # ファイルを保存
        with open(fname, "wb") as f:
            f.write(response.body)
