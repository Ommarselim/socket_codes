import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define server address and port
server_address = ('localhost', 8888)

# Bind the socket to the server address
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)
print('Server started and listening for connections...')

# Wait for a client to connect
client_socket, client_address = server_socket.accept()
print('Client connected:', client_address)

# Initialize the Tic Tac Toe board
board = [' '] * 9

# Function to check for a win condition
def check_win(board):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]               # diagonals
    ]

    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return True

    return False

# Function to display the board
def display_board(board):
    print('---------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('---------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('---------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('---------')

# Main game loop
while True:
    # Receive the move from the client
    move = client_socket.recv(1024).decode().strip()

    # Update the board
    board[int(move)] = 'X'

    # Check for a win
    if check_win(board):
        display_board(board)
        print('You win!')
        client_socket.send('win'.encode())
        break

    # Check for a draw
    if ' ' not in board:
        display_board(board)
        print("It's a draw!")
        client_socket.send('draw'.encode())
        break

    # Display the updated board
    display_board(board)

    # Get the server's move
    while True:
        server_move = input('Enter your move (0-8): ')
        if server_move.isdigit() and int(server_move) >= 0 and int(server_move) <= 8 and board[int(server_move)] == ' ':
            break
        else:
            print('Invalid move. Try again.')

    # Update the board with the server's move
    board[int(server_move)] = 'O'

    # Send the server's move to the client
    client_socket.send(server_move.encode())

    # Check for a win
    if check_win(board):
        display_board(board)
        print('Server wins!')
        break

    # Check for a draw
    if ' ' not in board:
        display_board(board)
        print("It's a draw!")
        client_socket.send('draw'.encode())
        break

# Close the sockets
client_socket.close()
server_socket.close()
