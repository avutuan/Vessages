# client program
import socket
import threading

class IMClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
    
    def connect_to_server(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"[CONNECTED] Connected to {self.host}:{self.port}")
        except ConnectionRefusedError as e:
            print(f"[ERROR] Connection failed: {e}")
    
    def disconnect_from_server(self):
        if self.socket:
            self.socket.close()
            print("[DISCONNECTED] Disconnected from server")
        
    def receive_messages(self):
        while True:
            message = self.socket.recv(1024).decode('utf-8')
            if not message:
                self.disconnect_from_server()
                break
            print(message)
    
if __name__ == "__main__":
    client = IMClient('127.0.0.1', 12345)
    client.connect_to_server()
    threading.Thread(target=client.receive_messages).start()

    print("\nCommands:")
    print("1. Register user: REGISTER <username> <password>")
    print("2. Login user: LOGIN <username> <password>")
    print("3. Logout user: LOGOUT <username>")
    print("4. Get online users: WHO")
    print("5. Send message: SEND <receiver> <message>")
    print("6. Exit: EXIT")
    while True:
        try:
            command = input("Enter command: ")
            client.socket.send(command.encode('utf-8'))
            if command == "EXIT":
                break
        except:
            break
    client.disconnect_from_server()
        
        