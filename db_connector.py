import pymysql
import datetime
from flask import request


def Create_Table():
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    cursor = conn.cursor()
    conn.autocommit(True)
    name_table = "user"
    cursor.execute(
        "CREATE TABLE `Q2PbjAC1nT`.`" + name_table + "` (`ID` INT UNSIGNED NOT NULL,`name` VARCHAR(50) NOT NULL,`time_column_datetime` VARCHAR(50) NOT NULL)")
    print("Ready table " + name_table + "")
    cursor.close()
    conn.close()


def get_users(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    cursor = conn.cursor()
    conn.autocommit(True)
    x = cursor.execute("SELECT * FROM Q2PbjAC1nT.users;")
    result = cursor.fetchall()
    for row in result:
        show = str(row[1])
        if show == user_id:
            user_name = row[0]
            print("success get_users")
            return user_name
        else:
            print('Fail get_user')
    cursor.close()
    conn.close()

users = {}


def insert_user(user_id) :
    request_data = request.json
    user_name = request_data.get('user_name')
    users[user_id] = user_name
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    conn.autocommit(True)
    cursor = conn.cursor()
    now = datetime.datetime.utcnow()
    str_now = now.date().isoformat()
    cursor.execute("INSERT INTO Q2PbjAC1nT.users (`name`, `user_id` ,time ) VALUES (%s,%s,%s)", (user_name, user_id,str_now))
    # `time_column`
    cursor.close()
    conn.close()
    print("success insert_user")
    return user_name



users = {}


def update_user(user_id):
    request_data = request.json
    request_data.get('user_name')
    user_name = request_data.get('user_name')
    users[user_id] = user_name
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("UPDATE Q2PbjAC1nT.users SET name = '" + user_name + "'  WHERE user_id=" + user_id + "")
    cursor.close()
    conn.close()
    print("success update_user")

    return user_name


def delete_user(user_id):
    conn = pymysql.connect(host='remotemysql.com', port=3306, user='Q2PbjAC1nT', passwd='WRYn22HLYY', db='Q2PbjAC1nT')
    conn.autocommit(True)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Q2PbjAC1nT.users;")
    result = cursor.fetchall()
    for row in result:
        show = str(row[0])
        if show == user_id:
            print(row[1])
            user_name = row[1]
    cursor.execute("DELETE FROM Q2PbjAC1nT.users WHERE user_id = " + user_id + "")
    cursor.close()
    conn.close()
    print("success delete_user")
    return user_name



