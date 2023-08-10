import socket
import threading
import os

def handle_client(client_socket, client_address):
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                print(f"Client {client_address} disconnected")
                break
            elif data.startswith("file_unicast:") or data.startswith("file_multicast:") or data.startswith("file_broadcast:"):
                file_name = data.split(":")[1]
                save_file(client_socket, file_name)
                notify_file_received(client_socket, file_name)
            elif data.startswith("download:"):
                file_name = data[9:]
                send_file_to_client(client_socket, file_name)
            else:
                handle_message(client_socket, client_address, data)
        except Exception as e:
            print("Error:", e)
            break

    client_socket.close()
    try:
        clients.remove(client_socket)
    except ValueError:
        pass

def handle_message(client_socket, client_address, message):
    if message.startswith("unicast:"):
        recipient_address, message = message[8:].split(":")
        send_unicast(client_socket, client_address, recipient_address, message)
    elif message.startswith("multicast:"):
        message = message[10:]
        send_multicast(client_socket, client_address, message)
    else:
        send_broadcast(client_socket, client_address, message)

def save_file(client_socket, file_name):
    with open(f"received_files/{file_name}", "wb") as f:
        while True:
            file_data = client_socket.recv(1024)
            if not file_data:
                break
            f.write(file_data)
    print(f"Received file: {file_name}")

def notify_file_received(sender_socket, file_name):
    for client_socket, client_address in clients:
        if client_socket != sender_socket:
            client_socket.send(f"file:{file_name}".encode('utf-8'))

def send_file_to_client(client_socket, file_name):
    try:
        with open(f"files_to_send/{file_name}", "rb") as f:
            file_data = f.read(1024)
            while file_data:
                client_socket.send(file_data)
                file_data = f.read(1024)
    except FileNotFoundError:
        print(f"File {file_name} not found on server")
    except Exception as e:
        print("Error sending file:", e)


def send_unicast(sender_socket, sender_address, recipient_address, message):
    for client_socket, client_address in clients:
        if client_address[0] == recipient_address:
            client_socket.send(f"{sender_address[0]}: {message}".encode('utf-8'))
            break

def send_multicast(sender_socket, sender_address, message):
    for client_socket, client_address in clients:
        if client_socket != sender_socket:  # Tidak mengirim ke pengirim
            client_socket.send(f"Multicast from {sender_address[0]}: {message}".encode('utf-8'))

def send_broadcast(sender_socket, sender_address, message):
    for client_socket, client_address in clients:
        if client_socket != sender_socket:  # Tidak mengirim ke pengirim
            client_socket.send(f"Broadcast from {sender_address[0]}: {message}".encode('utf-8'))

host = '10.217.18.147'
port = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"Server listening on {host}:{port}")

if not os.path.exists("received_files"):
    os.makedirs("received_files")

if not os.path.exists("files_to_send"):
    os.makedirs("files_to_send")

clients = []

while True:
    client_socket, client_address = server.accept()
    print(f"Accepted connection from: {client_address}")
    clients.append((client_socket, client_address))

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
