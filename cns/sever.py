import socket

host = "127.0.0.1"
port = 6902
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(0)
print("Server started at", host, "/", port)

conn, addr = server_socket.accept()
print(f"message from {addr}")
while True:
    req = conn.recv(1024).decode()
    print("request: ",req)
    if req == "close":
        conn.send("closed".encode())
        break
    elif req == 'file':
        write_file = open("server_file.txt", "w")
        file_line = conn.recv(1024).decode()
            # if(file_line == "EOF"):
            #     break
        write_file.writelines(file_line)
        write_file.close()
        conn.send(f"file received! {write_file.name}".encode())
    elif req == 'calculate':
        conn.send("calculating...".encode())
        req = conn.recv(1024).decode()
        output = eval(req)
        conn.send(f"{req} = {output}".encode())
    else:
        conn.send("HELLO THERE!!!".encode())
    
conn.close()
server_socket.close()