import requests, json

# LINE Messaging API 的 Channel Access Token
channel_access_token = 'ZUp+jnv9shnZyXpw1jESXABkK9lq3cKLtJPstbwXoVj5SeEILt1hEcIJHUchjUx+fSlLitDKNy4fsChfKnhWobb0SGQPsVElaNSVSwCQ4QJwuzLxlqL7ANEMb4e0hTrexsohZVe7eOVZ6g65BLazQQdB04t89/1O/w1cDnyilFU='

# 目標使用者的 LINE ID
user_id = 'a21xz02'

# 訊息內容
message = {
    'type': 'text',
    'text': '你好，這是一條自動發送的訊息！87'
}

# 設定標頭
headers = {
    'Authorization': f'Bearer {channel_access_token}',
    'Content-Type': 'application/json'
}

# 準備發送的訊息
body = {
    'to': user_id,
    'messages': [message]
}

# 發送 POST 請求，使用 json 參數直接傳遞字典
response = requests.post('https://api.line.me/v2/bot/message/push', headers=headers, json=body)

# 印出 API 回應
print(response.text)
