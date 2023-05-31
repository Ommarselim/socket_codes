import socket
import threading
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message:
                break
            print('Received:', message)
        except ConnectionResetError:
            print('Disconnected from the chat')
            break

def start_client():
    host = '127.0.0.1'
    port = 12345
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    client_socket.connect((host, port))
    print('Connected to server on {}:{}'.format(host, port))
    # Start a separate thread to receive messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()
    while True:
        # Send a message to the server
        message = input('Client: ')
        client_socket.send(message.encode())
    # Close the connection
    client_socket.close()
if __name__ == '__main__':
    start_client()