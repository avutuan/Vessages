# client program
import socket

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
    
    def send_command(self, command):
        try:
            self.socket.sendall(command.encode('utf-8'))
            return self.socket.recv(1024).decode('utf-8')
        except Exception as e:
            print(f"[ERROR] Failed to communicate with the server: {e}")
            return None
    
    def register_user(self, username, password):
        response = self.send_command(f"REGISTER {username} {password}")
        print(f"Server reponse: {response}")
    
    def login_user(self, username, password):
        response = self.send_command(f"LOGIN {username} {password}")
        print(f"Server reponse: {response}")
    
    def logout_user(self, username):  
        response = self.send_command(f"LOGOUT {username}")
        print(f"Server reponse: {response}")
    
    def get_online_users(self):
        response = self.send_command("WHO")
        print(f"Online users: {response}")
    
    def send_message(self, sender, receiver, message):
        response = self.send_command(f"SEND {receiver} {message}")
        print(f"Server reponse: {response}")
    
if __name__ == "__main__":
    client = IMClient('127.0.0.1', 12345)
    client.connect_to_server()
    
    try:
        while True:
            print("\nCommands:")
            print("1. Register user: REGISTER <username> <password>")
            print("2. Login user: LOGIN <username> <password>")
            print("3. Logout user: LOGOUT <username>")
            print("4. Get online users: WHO")
            print("5. Send message: SEND <receiver> <message>")
            print("6. Exit: EXIT")
            
            command = input("Enter command: ")
            if command == "EXIT":
                break
            elif command.startswith("REGISTER"):
                _, username, password = command.split()
                client.register_user(username, password)
            elif command.startswith("LOGIN"):
                _, username, password = command.split()
                client.login_user(username, password)
            elif command.startswith("LOGOUT"):
                _, username = command.split()
                client.logout_user(username)
            elif command == "WHO":
                client.get_online_users()
            elif command.startswith("SEND"):
                _, receiver, message = command.split()
                client.send_message("user1", receiver, message)
            else:
                print("Invalid command")
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect_from_server()
        
        