import socket
import threading

def handle_client(client_socket, address):
    print(f"Connection established with {address}")
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received from {address}: {message}")
        if message == 'quit':
            break
        client_socket.send(message.encode('utf-8'))
    client_socket.close()
    print(f"Connection with {address} closed")

def start_server(host='localhost', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen()
    print(f"Server listening on {host}:{port}")
    try:
        while True:
            client_socket, address = server_socket.accept()
            thread = threading.Thread(target=handle_client, args=(client_socket, address))
            thread.start()
            print(f"Active connections: {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("Server is closing.")
        server_socket.close()

if __name__ == "__main__":
    start_server()

