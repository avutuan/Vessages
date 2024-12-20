# server program
import socket
import threading
import database

HOST = '127.0.0.1'
PORT = 12345

users = {}

online_users = {}

def load_users():
    conn = database.create_connection()
    c = conn.cursor()
    
    c.execute('''
        SELECT username FROM users WHERE status = 'online'
    ''')
    users = c.fetchall()
    for user in users:
        online_users[user[0]] = None
        
    conn.close()

def handle_client(client_socket, client_address):
    username = None
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        while True:
            # Receive data
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            
            command, *args = message.split()
            if command == "REGISTER":
                if len(args) < 2:
                    response = "Error: Invalid command"
                username, password = args
                if username in users:
                    response = "Error: User already registered"
                else:
                    users[username] = password
                    response = database.register_user(*args)
            elif command == "LOGIN":
                if len(args) < 2:
                    response = "Error: Invalid command"
                username, password = args
                if username not in users or users[username] != password:
                    response = "Error: Invalid credentials"
                else:
                    online_users[username] = client_socket
                    response = database.login_user(*args)
                response = database.login_user(*args)
            elif command == "LOGOUT":
                response = database.logout_user(*args)
                if username in online_users:
                    del online_users[username]
                break
            elif command == "WHO":
                response = database.get_online_users()
            elif command == "SEND":
                if username is None:
                    response = "Error: You are not logged in"
                    continue
                if len(args) < 2:
                    response = "Error: Invalid command"
                    continue
                rcvr, message = args[0], ' '.join(args[1:])
                if rcvr in online_users:
                    online_users[rcvr].send(f"{username}: {message}".encode('utf-8'))
                else:
                    response = "Error: User is not online"
            else:
                response = "Invalid command"
            
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"[ERROR] {client_address} disconnected: {e}")
    finally:
        if username in online_users:
            del online_users[username]
        
        client_socket.close()
        
        
def start_server():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        try:
            client_socket, client_address = server.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            thread.start()
        except OSError as e:
            print(f"[ERROR] Failed to accept connection: {e}")
            break
    
if __name__ == "__main__":
    start_server()
    