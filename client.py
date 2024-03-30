import socket

def start_client(host='localhost', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to the server. Type 'quit' to exit.")
        while True:
            message = input("Message: ")
            client_socket.send(message.encode('utf-8'))
            if message == 'quit':
                break
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Server response: {response}")

if __name__ == "__main__":
    start_client()

