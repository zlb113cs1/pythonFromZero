import requests
import json

# 用你的 access token 替换下面的字符串
access_token = 'your_access_token_here'

graph_endpoint = 'https://graph.microsoft.com/v1.0'

headers = {
    'Authorization': 'Bearer ' + access_token,
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# 获取当前用户的 profile
response = requests.get(
    url=f"{graph_endpoint}/me", 
    headers=headers
)

if response.status_code == 200:
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Request failed. {response.status_code}, {response.text}")
