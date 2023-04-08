import socket
import threading
header=64
port=5050
format="utf-8"
dc="!disconnect"
server=socket.gethostbyname(socket.gethostname())  #SET_IP
ADDR=(server,port)
server1=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server1.bind(ADDR)
def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected=True

    while connected:
        msg_length=conn.recv(header).decode(format)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(format)
            if msg==dc:
                connected=False
            print(f"[{addr}] {msg}")
            # Send the data to Arduino
    conn.close()


def start():
    server1.listen()
    print(f"server is listening {server}")
    while True:
        conn,addr=server1.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTION]{threading.activeCount()-1}")

print("[STARTING] server is starting.....")
start()
