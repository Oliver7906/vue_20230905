import requests, json
# 要先安裝requests模組 指令如下:pip install requests

# 注意前方要有 Bearer
headers = {'Authorization':'Bearer ZUp+jnv9shnZyXpw1jESXABkK9lq3cKLtJPstbwXoVj5SeEILt1hEcIJHUchjUx+fSlLitDKNy4fsChfKnhWobb0SGQPsVElaNSVSwCQ4QJwuzLxlqL7ANEMb4e0hTrexsohZVe7eOVZ6g65BLazQQdB04t89/1O/w1cDnyilFU=','Content-Type':'application/json'}
body = {
    'to':'a21xz02',
    'messages':[{
            'type': 'text',
            'text': 'hello'
        }]
    }
# 向指定網址發送 request
req = requests.request('POST', 'https://api.line.me/v2/bot/message/push',headers=headers,data=json.dumps(body).encode('utf-8'))
# 印出得到的結果
print(req.text)