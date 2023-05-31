import socket

def start_server():
    host = '127.0.0.1'
    port = 12345
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host} and port {port} ")
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print(f'Connected to client:{addr}')
    while True:
        # Receive data from the client
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print('Client:', data)
        # Send a response back to the client
        response = input('Server: ')
        client_socket.send(response.encode())
    # Close the connection
    client_socket.close()
if __name__ == '__main__':
    start_server()
