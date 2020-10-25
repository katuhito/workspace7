import scrapy

# Spiderを継承してクラスを作る
class Soseki2Spider(scrapy.Spider):
    name = 'soseki2'
    start_urls = ['https://www.aozora.gr.jp/index_pages/person148.html']

    def parse(self, response):
        li_list = response.css('ol > li a')
        for a in li_list:
            href = a.css('::attr(href)').extract_first()
            text = a.css('::text').extract_first()
            # フルパスに変換
            href2 = response.urljoin(href)
            # 結果を返す
            yield {
                'text': text,
                'url': href2
            }
