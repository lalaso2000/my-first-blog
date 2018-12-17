import json
import urllib.request

url = 'http://127.0.0.1:8000/api/posts/'

data = {
    'author': 1,
    'title': 'apiテスト',
    'text': 'ほんとかなぁ？',
    'created_date': '2018-12-17T14:00:00.000000+09:00',
    'published_date': '2018-12-17T14:00:00.000000+09:00',
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
