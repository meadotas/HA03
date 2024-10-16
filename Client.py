import socket

def client_program():
    # Get the hostname (local machine)
    host = socket.gethostname()
    port = 5001

    # Create a new instance of the socket
    client_socket = socket.socket()
    # Connect to the server
    client_socket.connect((host, port))

    print("Connected to the server...")
    print("Send a message or type 'Send File' to transfer a file")

    while True:
        # User input for message or file command
        message = input("Client ->")

        # Send the message
        client_socket.send(message.encode())

        # If the client wants to send a file
        if message.lower() == 'send file':
            file_name = input("Enter the file name to send: ")
            client_socket.send(file_name.encode())

            with open(file_name, 'rb') as file:
                file_data = file.read(4096)
                client_socket.send(file_data)
            print(f"File '{file_name}' sent successfully.")

        # The client wants to end the connection
        elif message.lower() == 'bye' or message.lower() == 'goodbye':
            break
        else:
            server_response = client_socket.recv(1024).decode()
            print(f"From Server: {server_response}")

    # Close the client connection
    client_socket.close()

if __name__ == '__main__':
    client_program()