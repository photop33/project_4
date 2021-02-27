import requests
import pymysql
user_id= "8"
user_name='lior'


res = requests.post(f'http://{host}:{port}/users/{id}', json={"user_name": f'{user_name}'})
print("post response -", res.json())
    
    
res = requests.get('http://127.0.0.1:5005/user/'+ user_id  +'')
if res.ok:
    print(res.json())


    

conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
conn.autocommit(True)
cursor = conn.cursor()
x=cursor.execute("SELECT * FROM Q2PbjAC1nT.users WHERE user_id;")
if x==user_id:
    y = cursor.fetchall()
    user_name = y[0]
    print (user_name)
    
