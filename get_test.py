import urllib.request
import json

url = 'http://127.0.0.1:8000/api/posts/'

# リクエストを投げる
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = res.read()

# データを辞書形式に変更
data = json.loads(body)

# 1つ1つ取り出してみる
for d in data:
    print(d['title'])
