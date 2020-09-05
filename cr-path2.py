from urllib.parse import urljoin

base = "https://example.com/html/a.html"

print(urljoin(base, "/hoge.html"))
print(urljoin(base, "http://kujirahand.com/wiki"))
print(urljoin(base, "//uta.pw/shodow"))
