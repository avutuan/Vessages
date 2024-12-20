# server program
import socket
import threading
import database

HOST = '127.0.0.1'
PORT = 12345

def handle_client(client_socket, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.")
    try:
        while True:
            # Receive data
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"[{client_address}] {message}")
            
            # Process message here (e.g. send to another client)
            response = "Message received."
            client_socket.send(response.encode('utf-8'))
    except ConnectionResetError:
        print(f"[DISCONNECTED] {client_address}")
    finally:
        client_socket.close()
        
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}")
    
    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()
        
def register_user(username, password):
    return database.register_user(username, password)

def login_user(username, password):
    return database.login_user(username, password)

def logout_user(username):
    return database.logout_user(username)

def get_online_users():
    return database.get_online_users()

def send_message(sender, receiver, message):
    if receiver not in get_online_users():
        return f"Error: {receiver} is not online"
    receiver_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receiver_socket.connect((HOST, PORT))
    receiver_socket.send(f"{sender} to {receiver}: {message}".encode('utf-8'))
    return "Message sent"
    
if __name__ == "__main__":
    start_server()