import socket
import threading
def handle_client(client):

    while True:
        try:
            msg = client.recv(1024).decode('utf')
            if not msg:
                break

            print("Received: " +msg)

            #Broadcast it 

            for client in clients:
                client.send(msg.encode('utf'))
        except:
            break






def StartServer():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 12345
    server_socket.bind((host, port))
    print("Starting server")
    server_socket.listen(5)
    print("Waiting for connections...")

    while True:
        client,addr = server_socket.accept()
        clients.append(client)
        handle_client_thread = threading.Thread(target=handle_client, args=(client,))
        handle_client_thread.start()

        














if __name__ == "__main__":
    clients = []
    StartServer()

    