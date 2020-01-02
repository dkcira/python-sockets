#!/usr/bin/env python3
# test with 'curl localhost:8080'
import socket
import time
import _thread

SERVER_PORT=8080
print(f"listening on localhost:{SERVER_PORT}")

s = socket.socket()
# to avoid address already in use when restarting the server
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", SERVER_PORT))
s.listen(10) # 10 is the backlog

# write a valid http response
http_response = b"""HTTP/1.1 200 OK\r
Content-Length: 10\r

hi there!\n\r\n"""

def respond(conn):
    # print out once we get the connection
    print(str(conn.recv(4096)))
    # introduce a wait to simulate slow communication, server response, etc
    time.sleep(0.5)
    # send response
    conn.send(http_response)
    # shutdown, close the connection
    conn.shutdown(socket.SHUT_WR)
    conn.close()


while True:
    # wait for a connection
    conn, address = s.accept()
    # start new thread to respond to connection and go back to wait for new connection
    _thread.start_new_thread(respond, (conn,))


# close socket
s.close()