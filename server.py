import socket

HOST = 'localhost'
PORT = 8080

def handle_request(request):
    # Process the request and generate the appropriate response
    response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\nThis is the receiving end'
    return response.encode()

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((HOST, PORT))

    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(HOST, PORT))

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print('Connected by', client_address)

        # Receive data from the client
        request_data = client_socket.recv(1024).decode()

        # Handle the request and get the response
        response_data = handle_request(request_data)

        # Send the response back to the client
        client_socket.sendall(response_data)

        # Close the connection with the client
        client_socket.close()

    # Close the server socket
    server_socket.close()

if __name__ == '__main__':
    start_server()


