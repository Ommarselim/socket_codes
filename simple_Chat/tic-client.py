import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the server address and port
server_address = ('localhost', 8888)

# Connect to the server
client_socket.connect(server_address)
print('Connected to the server:', server_address)

# Main game loop
while True:
    # Receive the server's move
    server_move = client_socket.recv(1024).decode()

    # Check for a win or draw
    if server_move == 'win':
        print('You lose!')
        break
    elif server_move == 'draw':
        print("It's a draw!")
        break

    # Display the server's move
    print('Server\'s move:', server_move)

    # Get the client's move
    while True:
        client_move = input('Enter your move (0-8): ')
        if client_move.isdigit() and int(client_move) >= 0 and int(client_move) <= 8:
            break
        else:
            print('Invalid move. Try again.')

    # Send the client's move to the server
    client_socket.send(client_move.encode())

# Close the socket
client_socket.close()
