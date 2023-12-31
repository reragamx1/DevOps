import socket
import json
def main():
    fun_info()
def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config
def fun_info():
    config = read_config('config_file.json')
    server_info = config['servers'][0]
    ip = server_info['ip']
    port = server_info['port']
    SIZE = config['max_buffer_size']

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(10)
    print(f"Server listening on {ip}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
       # print(f"Connection established with {client_address}")

        try:
            data = client_socket.recv(SIZE).decode()
            print("received from client:", data)
            if data == 'exit':
                print("Client sent 'exit', so client connection is closed. ")
                break

            response = f" serviceprovider received: {data}"
            client_socket.send(response.encode())
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            client_socket.close()

    server_socket.close()

if __name__ == "__main__":
    main()
