import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 12345))
message = s.recv(1024)
# This 1024 is for byte and not the port number
print(message.decode("utf-8"))