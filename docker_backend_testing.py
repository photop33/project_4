import requests
import db_connector

user_id = "8"
user_name = 'lior'

res = requests.get('http://127.0.0.1:5002/user/' + user_id + '')
if res.ok:
    print(res.json())

x = db_connector.get_users(user_id)
print(x)
