import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print('Received:', message)

            # Send the message to all other connected clients
            for client in clients:
                if client != client_socket:
                    client.send(message.encode())
        except ConnectionResetError:
            break

    # Remove the client from the list
    clients.remove(client_socket)
    client_socket.close()

def start_server():
    host = '127.0.0.1'
    port = 12345

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print('Server listening on {}:{}'.format(host, port))

    while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print('Connected to client:', addr)

        # Add the client to the list
        clients.append(client_socket)

        # Start a separate thread to handle the client
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

    # Close the server socket
    server_socket.close()

if __name__ == '__main__':
    clients = []
    start_server()
