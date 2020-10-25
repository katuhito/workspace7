from scrapy.http import HtmlResponse
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# FireFoxの初期化
driver = Firefox()

# FireFoxで任意のURLを開く
def selenium_get(url):
    driver.get(url)

# CSSクエリを指定して読み込みが完了するまで待機
def get_dom(query):
    dom = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, query)))
    return dom

# Firefoxを閉じる
def selenium_close():
    driver.close()

# ミドルウエアの本体
class SeleniumMiddleware(object):
    # リクエストをSeleniumで処理する
    def process_request(self, request, spider):
        driver.get(request.url)
        return HtmlResponse(
            driver.current_url,
            body = driver.page_source,
            encoding = 'utf-8',
            request = request
        )
        
