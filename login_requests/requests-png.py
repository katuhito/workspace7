import requests
r = requests.get("https://uta.pw/shodouy/imp/3/3.png")

with open("test.png", "wb") as f:
    f.write(r.content)

print("saved")

