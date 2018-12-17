'''POSTのテスト

引数は
「タイトル」
「テキスト」
「ファイルの絶対パス」

'''

import requests
import sys
from datetime import datetime, timedelta, timezone
import os
import mimetypes

args = sys.argv
if len(args) != 4:
    print('>> Illegal argument Error!!')
    quit()

# 時間取得
JST = timezone(timedelta(hours=+9), 'JST')

# 制作時間
created_date = datetime.now(JST).isoformat()

# ファイル取得
fileName = args[3]
baseName = os.path.basename(fileName)
MIMETYPE = mimetypes.guess_type(baseName)[0]
fileDataBinary = open(fileName, 'rb').read()

# 公開時間（ここで設定するのは間違いだけど…）
published_date = datetime.now(JST).isoformat()

data = {
    'author': 1,
    'title': args[1],
    'text': args[2],
    'created_data': created_date,
    'published_date': published_date,
}

files = {'attach': (baseName, fileDataBinary, MIMETYPE)}

url = 'http://127.0.0.1:8000/api/posts/'
response = requests.post(url, data=data, files=files)

print(response.status_code)
print(response.content)
