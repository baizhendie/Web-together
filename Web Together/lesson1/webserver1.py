#coding:utf-8
'''
Created on 2017年3月29日

@author: Bai
'''
import socket
 
HOST = ''
PORT = 8888
 
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print ('Serving HTTP on port %s ...' % PORT)
while True:
    client_connection, client_address = listen_socket.accept()
    #print(client_connection)
    #print(client_address)
    request = client_connection.recv(1024)
    print (request)
 
    http_response_data = """HTTP/1.1 200 OK

 
Hello, World!
"""
    http_response = http_response_data.encode(encoding='utf_8')
    client_connection.sendall(http_response)
    client_connection.close()