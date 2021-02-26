import requests
user_id= "1"
user_name= 'Daniel'

res = requests.post('http://127.0.0.1:8000/user/'+ user_id +'', json={"user_name": ""+ user_name +""})
if res.ok:
    print(res.json())



res = requests.get('http://127.0.0.1:8000/user/'+ user_id  +'')
if res.ok:
    print(res.json())
    
