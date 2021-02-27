import requests
import pymysql
user_id= "8"


res = requests.get('http://127.0.0.1:5000/user/'+ user_id  +'')
if res.ok:
    print(res.json())


    
