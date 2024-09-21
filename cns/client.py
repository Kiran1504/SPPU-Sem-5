import socket

host = "127.0.0.1"
port = 6902

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
# client_socket.listen(0)

opp = int(input("ENTER OPERATION (exit to STOP): "))
while(opp != -1):
    if(opp == 1):
        client_socket.send("HIII SERVER!!!".encode())
        resp = client_socket.recv(1024).decode()
        print(f"response from server: {resp}")

    elif opp == 2:
        read_file = open("client_file.txt", "r")
        client_socket.send("file".encode())
        data = read_file.read()
        if not data:
            break
        else:
            client_socket.send(data.encode())
        # client_socket.send("EOF".encode())
        resp = client_socket.recv(1024).decode()
        print(f"response from server: {resp}")
    elif opp == 3:
        client_socket.send("calculate".encode())
        resp = client_socket.recv(1024).decode()
        print(f"response from server: {resp}")
        exp = input("Input the expression to be evalued: ")
        client_socket.send(exp.encode())
        resp = client_socket.recv(1024).decode()
        print(f"response from server: {resp}")
    opp = int(input("ENTER OPERATION (exit to STOP): "))
client_socket.send("close".encode())
client_socket.close()