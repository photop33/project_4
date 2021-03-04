import requests
user_id = "1"

res = requests.get('http://127.0.0.1:6000/user/' + user_id + '')
if res.ok:
    print(res.json())

    
