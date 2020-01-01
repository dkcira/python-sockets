#!/usr/bin/env python3
import socket

s = socket.socket()
# 93.184.216.34 => example.com
s.connect(("93.184.216.34", 80))
s.send(b"GET / HTTP/1.1\r\nHost: example.com\r\n\r\n")
print(str(s.recv(4096)))