import requests
import sys
from datetime import datetime, timedelta, timezone
import os

# 時間取得
JST = timezone(timedelta(hours=+9), 'JST')

# 制作時間
created_date = datetime.now(JST).isoformat()

# ファイル取得
args = sys.argv
fileName = args[1]
baseName = os.path.basename(fileName)
MINETYPE = 'application/png'
fileDataBinary = open(fileName, 'rb').read()

# 公開時間（ここで設定するのは間違いだけど…）
published_date = datetime.now(JST).isoformat()

data = {
    'author': 1,
    'title': 'api＋ファイルアップロード',
    'text': 'これができたら終わり！',
    'created_data': created_date,
    'published_date': published_date,
}

files = {
    'attach': (baseName, fileDataBinary, MINETYPE)
}

url = 'http://127.0.0.1:8000/api/posts/'
response = requests.post(url, data=data, files=files)

print(response.status_code)
print(response.content)
