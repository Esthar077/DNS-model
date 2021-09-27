# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 16:20:40 2021

@author: Esthar
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.43.154", 1234))

req_u = s.recv(1024)
url = input(str(req_u.decode("utf-8")))
s.send(bytes(url,"utf-8"))
rep = s.recv(1024)
print(rep.decode("utf-8"))