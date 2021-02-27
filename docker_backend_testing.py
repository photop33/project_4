import requests

user_id = "8"


    

res = requests.get('http://127.0.0.1:4009/user/'+ user_id  +'')
if res.ok:
    print(res.json())

res = requests.get('http://127.0.0.1:5002/user/'+ user_id  +'')
if res.ok:
    print(res.json())

    
conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
cursor = conn.cursor()
conn.autocommit(True)
x = cursor.execute("SELECT * FROM Q2PbjAC1nT.users;")
result = cursor.fetchall()
for row in result:
    show = str(row[1])
    print(show,user_id)
    if show == user_id:
        user_name = row[0]
        print(user_name)
