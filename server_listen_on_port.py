#!/usr/bin/env python3
# test with 'curl localhost:8080'
import socket

s = socket.socket()
# to avoid address already in use when restarting the server
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8080))
s.listen(10) # 10 is the backlog

# wait for a connection
conn, address = s.accept()
# print out once we get the connection
print(str(conn.recv(4096)))

# shutdown, close the connection and the socket
conn.shutdown(socket.SHUT_RDWR)
conn.close()
s.close()