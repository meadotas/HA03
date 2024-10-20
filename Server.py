import socket

# Using the provided documentation given through Canvas:
# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

def server_program():
    # get the hostname (local machine)
    host = socket.gethostname()
    port = 5001

    # Create a socket instance
    server_socket = socket.socket()

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    #Listen for connections
    server_socket.listen(2)
    
    print(f"Server is running on {host}:{port}, waiting for a connection...")
    # Accept new connection
    connection, address = server_socket.accept()
    print(f"Connection from: {address}")

    while True:
        # Receive data (message or file command) from the client
        data = connection.recv(1024).decode()
        if not data:
            # If the data is not received, break
            break

        print(f"Client: {data}")

        # If the received data was a goodbye message then break out of the connection
        if data.lower() == 'bye' or data.lower() == 'goodbye':
            break

        # Check if received data from the client is of the command send file
        if data.lower() == 'send file':

            # Receive the file name from the client (up to 1024 bytes)
            # Decode the received bytes into a string to get the file name
            file_name = connection.recv(1024).decode()
            # Receive the file data from the client (up to 4096 bytes)
            file_data = connection.recv(4096)
            # Open a new file in write-binary mode with the name prefixed by 'received'
            with open(f'received_{file_name}', 'wb') as file:
                # Write the received data to the new file
                file.write(file_data)
                # Print confirmation message
                print(f"File '{file_name}' received successfully.")
        else:
            # Otherwise the data received was not a 'send file"
            # Server sends a reply message to the client
            message = input("Server -> ")
            # Encode the data and send it back to the client
            connection.send(message.encode())

    # Close the connection
    connection.close()
    print("Server connection closed.")

if __name__ == '__main__':
    server_program()