import socket
host='127.0.0.1'
port=5000

filename=input('enter filename:')
with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
    s.connect((host,port))
    s.sendall(filename.encode())
    data=s.recv(4096)
    print('File content:\n')
    print(data.decode())

