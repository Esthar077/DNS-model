# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:15:01 2021

@author: Esthar
"""

import mysql.connector
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)
print("Waiting for incoming connections...")
//accepting client
clientsocket, address = s.accept()
print(f"Connection from {address} has been established!")
clientsocket.send(bytes("Enter url: ","utf-8"))
url = clientsocket.recv(1024)
url=url.decode("utf-8")
//creating database connection
myconn = mysql.connector.connect(host="localhost",user="esthar",passwd="pass#123",database="DNS")
print("Database connection establised")
cur = myconn.cursor()
cur.execute("select count(ip_address) from dns where url=\""+url+"\"")
for x in cur:
    count=x[0]
if(count>0):
    try:
        //selecting ip_address from table where url = given url
        cur.execute("select ip_address from dns where url=\""+url+"\"")
    except:
        myconn.rollback()
    for x in cur:
         clientsocket.send(bytes("ip-address: "+x[0],"utf-8"))
//cannot find any matching url
else:
    clientsocket.send(bytes("invalid url","utf-8"))
myconn.close()
