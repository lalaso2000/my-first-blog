import json
import requests

url = 'http://127.0.0.1:8000/api/posts/'

# リクエストを投げる
response = requests.get(url)

# 結果を見てみる
print('status_code : {}'.format(response.status_code))

data = response.json()

print(json.dumps(data, indent=4))
