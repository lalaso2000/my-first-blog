import json
import urllib.request
from datetime import datetime as dt, timezone, timedelta

url = 'http://127.0.0.1:8000/api/posts/'

# 現在時刻取得
JST = timezone(timedelta(hours=+9), 'JST')
timestr = dt.now(JST).isoformat()
print(timestr)

# postデータ生成
data = {
    'author': 1,
    'title': 'apiテスト2',
    'text': 'ほんとだね',
    'created_date': timestr,
    'published_date': timestr,
}

headers = {
    'Content-Type': 'application/json',
}

print(json.dumps(data))

req = urllib.request.Request(url, json.dumps(data).encode('utf-8'), headers)
with urllib.request.urlopen(req) as res:
    body = res.read()

ans = json.loads(body)

print(ans)
