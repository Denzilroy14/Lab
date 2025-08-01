import socket
import os

host='127.0.0.1'
port=5000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
    s.bind((host,port))
    s.listen()
    print(f'Server listening on {host} at:{port}')
    conn,addr=s.accept()
    with conn:
        print(f'connected by:{addr}')
        filename=conn.recv(1024).decode()
        if os.path.exists(filename):
            with open(filename,'r')as f:
                content=f.read()
                conn.sendall(content.encode())
        else:
            print('Error:Could not find file')

