#!/usr/bin/env python3
# coding=utf-8

import mysql.connector

conn = mysql.connector.connect(user='root',database='xiyou')
cursor = conn.cursor()
cursor.execute('select * from info')
values = cursor.fetchall()
print(values)

cursor.close()
conn.close()

