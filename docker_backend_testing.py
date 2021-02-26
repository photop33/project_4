  import requests
user_id= "8"


res = requests.get('http://127.0.0.1:8000/user/'+ user_id +'', json={"user_name": ""+ user_name +""})
if res.ok:
    print(res.json())



    
