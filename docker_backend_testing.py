import requests
user_id= "5"

res = requests.get('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())
    
