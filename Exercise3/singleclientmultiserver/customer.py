"""in this client program written to handle
multiple servers when host send the message should go to two differet servers run on python3 filename"""
import socket
import threading
import json

def main():
    send_message()
def read_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config
def send_message():
    try:
        config = read_config('config_file.json')
        SIZE = config['max_buffer_size']
        while True:
            message = input("Enter the broadcast message : ")
            if message == 'exit':
                send_exit_message(config,SIZE)
                break

            threads = []
            for server_info in config['servers']:
                thread = threading.Thread(target=send_broadcast_message, args=(server_info, message, SIZE))
                threads.append(thread)
                thread.start()

                for thread in threads:
                    thread.join()

    except Exception as e:
        print(f"An error occurred: {e}")

def send_broadcast_message(server_info, message,SIZE):
    try:
        ip = server_info['ip']
        port = server_info['port']
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((ip, port))
#        print (f"[CONNECTED] client connected to server at {ip} : {port}")
        client_socket.send(message.encode())
        if message != 'exit':
            response = client_socket.recv(SIZE).decode()
            print(f"Response from {ip}:{port}: {response}")

        client_socket.close()
    except Exception as e:
        print(f"Error connecting to {ip}:{port}: {e}")


def send_exit_message(config,SIZE):
    for server_info in config['servers']:
        send_broadcast_message(server_info, 'exit', SIZE)


if __name__ == "__main__":
    main()
